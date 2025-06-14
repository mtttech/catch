"""
Catch

Author:     Marcus T Taylor <mtaylor9754@hotmail.com>
Created:    16.11.23
Modified:   12.06.25
"""

import sys
import time
from typing import Any, Dict, List

from bs4 import BeautifulSoup
from prettytable import PrettyTable  # pyright: ignore
import requests

from catch.database import Fighter


def construct_table(stats: List[Any]) -> PrettyTable:
    table = PrettyTable()
    table.field_names = [
        "Athlete",
        "Wins",
        "Losses",
        "Draws",
        "Total",
        "Fight Win Streak",
        "First Round Finishes",
        "Wins by Knockout",
        "Wins by Submission",
        "Title Defenses",
    ]
    table.add_row(stats)
    return table


def request_url(athlete: str) -> bytes:
    athlete_tag = athlete.strip().lower().replace(" ", "-")
    resp = requests.get("https://www.ufc.com/athlete/" + athlete_tag)
    return resp.content


def scrape_stats(athlete: str, content: bytes) -> Dict[str, Any]:
    record = {}
    record["athlete"] = athlete

    # Gather the basic stats from the page.
    soup = BeautifulSoup(content, "html.parser")
    page_elems = soup.find("p", class_="hero-profile__division-body")
    record_string = page_elems.text.split(" ")  # pyright: ignore

    # Convert values in list to int.
    # Create entry with a total of the basic stats.
    record_values = [int(n) for n in record_string[0].split("-")]
    record["total"] = sum(record_values)

    # Fill in the basic category values.
    base_categories = ["wins", "losses", "draws"]
    for index, _ in enumerate(base_categories):
        record[base_categories[index]] = record_values[index]

    ### Gather/define additional possible stat categories.
    # Wins by Knockout
    # Wins by Submission
    # Wins by Decision
    # First Round Finishes
    # Fight Win Streak
    # Title Defenses
    stat_headings = soup.find_all("p", class_="hero-profile__stat-text")
    stat_headings = [x.text.lower().replace(" ", "_") for x in stat_headings]

    # Gather all the values for the above.
    stat_values = soup.find_all("p", class_="hero-profile__stat-numb")
    stat_values = [int(s.text) for s in stat_values]

    # Put it all together.
    for index, _ in enumerate(stat_headings):
        record[stat_headings[index]] = stat_values[index]

    # Populate non-specified categories, if necessary.
    for special_category in (
        "wins_by_knockout",
        "wins_by_submission",
        "wins_by_decision",
        "first_round_finishes",
        "fight_win_streak",
        "title_defenses",
    ):
        if special_category not in record:
            record[special_category] = 0

    # Sort the fighter records consistently.
    stat_order = [
        "athlete",
        "wins",
        "losses",
        "draws",
        "total",
        "fight_win_streak",
        "first_round_finishes",
        "wins_by_knockout",
        "wins_by_submission",
        "title_defenses",
    ]
    fighter_stats = {k: record[k] for k in stat_order if k in record}

    return fighter_stats


def catch_main() -> None:
    fighters = sys.argv
    if len(fighters) < 2:
        print("error: not enough arguments specified.")
        exit(1)

    for athlete in fighters[1:]:
        print(f"Looking up {athlete}...")
        resp = request_url(athlete)
        try:
            result = scrape_stats(athlete, resp)
            print(f"Stats found.")
            print(construct_table(list(result.values())))
            Fighter(result)
        except AttributeError:
            print(f"Nothing found for '{athlete}'.")

        time.sleep(1)
