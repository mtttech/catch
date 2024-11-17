"""
openfight
Author:     Marcus T Taylor <mtaylor9754@hotmail.com>
Created:    16.11.23
Modified:   17.11.24
"""
import sys
import time
from typing import Dict, Union

from bs4 import BeautifulSoup
import requests

BASE_URL = "https://www.ufc.com/athlete/"


def build_stat_block(athlete: str, content: bytes) -> Dict[str, Union[str, int]]:
    record = dict()
    record["athlete"] = athlete

    # Gather the basic stats from the page.
    soup = BeautifulSoup(content, "html.parser")

    fighter_record = soup.find("p", class_="hero-profile__division-body")
    fighter_record = fighter_record.text.split(" ") # pyright: ignore [reportOptionalMemberAccess]
    fighter_record = fighter_record[0].split("-")

    print(f"Stats found for {athlete}.")

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

    # Make the records consistent in order/return.
    order = [
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

    return {k: record[k] for k in order if k in record}


def request_fighter_stats(athlete: str) -> Union[Dict[str, Union[str, int]], None]:
    fighter_url = BASE_URL + athlete.strip().lower().replace(" ", "-")
    print(f"Looking up '{athlete}'...")
    try:
        result = requests.get(fighter_url)
        result.raise_for_status()
        time.sleep(1)
        return build_stat_block(athlete, result.content)
    except requests.exceptions.HTTPError as e:
        print(e.__str__())
    except AttributeError:
        print("A query error has occured.")


def openfight_main() -> None:
    athlete = sys.argv
    if len(athlete) < 2:
        print("error: not enough arguments specified.")
        exit(1)

    fighter_stats = [request_fighter_stats(a) for a in athlete[1:]]
    print(*fighter_stats)


if __name__ == "__main__":
    openfight_main()