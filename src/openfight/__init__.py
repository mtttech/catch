"""
openFIGHT
Author:     Marcus T Taylor <mtaylor9754@hotmail.com>
Created:    16.11.23
Modified:   22.11.24
"""

import sys
import time
from typing import Any, List

from bs4 import BeautifulSoup
from prettytable import PrettyTable  # pyright: ignore
import requests


def build_stat_block(athlete: str, content: bytes) -> List[Any]:
    record = dict()
    record["athlete"] = athlete

    # Gather the basic stats from the page.
    soup = BeautifulSoup(content, "html.parser")
    fighter_record = soup.find("p", class_="hero-profile__division-body")
    fighter_record = fighter_record.text.split(" ")  # pyright: ignore
    fighter_record = fighter_record[0].split("-")

    # Convert values in list to int.
    # Create entry with a total of the basic stats.
    record_values = [int(n) for n in fighter_record]
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
    other_categories = soup.findAll("p", class_="hero-profile__stat-text")
    other_categories = [x.text.lower().replace(" ", "_") for x in other_categories]

    # Gather all the values for the above.
    other_values = soup.findAll("p", class_="hero-profile__stat-numb")
    other_values = [int(s.text) for s in other_values]

    # Put it all together.
    for index, _ in enumerate(other_categories):
        record[other_categories[index]] = other_values[index]

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

    return list(fighter_stats.values())


def request_fighter_stats(athlete: str) -> List[Any] | None:
    try:
        fighter_url = "https://www.ufc.com/athlete/" + athlete.strip().lower().replace(
            " ", "-"
        )
        print(f"Looking up stats for '{athlete}'...")
        result = requests.get(fighter_url)
        result.raise_for_status()
        time.sleep(1)
        return build_stat_block(athlete, result.content)
    except requests.exceptions.HTTPError as e:
        print(e.__str__())
    except AttributeError:
        print(f"A query error has occured locating '{athlete}'.")


def openfight_main() -> None:
    athlete = sys.argv
    if len(athlete) < 2:
        print("error: not enough arguments specified.")
        exit(1)

    table = PrettyTable()
    table.field_names = [
        "",
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
    fighter_stats = [request_fighter_stats(a) for a in athlete[1:]]
    for stat in fighter_stats:
        try:
            table.add_row(stat)
        except TypeError:
            pass

    print(table)


if __name__ == "__main__":
    openfight_main()
