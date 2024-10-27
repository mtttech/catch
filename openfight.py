import asyncio
import sys

from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = "https://www.ufc.com/athlete/"


def parse_response(driver, athlete):
    record = dict()
    record["athlete"] = athlete

    assert athlete in driver.title

    # Gather the basic stats from the page.
    fighter_record = driver.find_element(By.CLASS_NAME, "hero-profile__division-body")
    fighter_record = fighter_record.text.split(" ")
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
    other_categories = driver.find_elements(By.CLASS_NAME, "hero-profile__stat-text")
    other_categories = [x.text.lower().replace(" ", "_") for x in other_categories]

    # Gather all the values for the above.
    other_values = driver.find_elements(By.CLASS_NAME, "hero-profile__stat-numb")
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


async def gather_requests(argv):
    async def request_athlete(athlete):
        fighter_url = BASE_URL + athlete.strip().lower().replace(" ", "-")
        print(f"Looking up ({athlete} @ {fighter_url})...")
        
        driver = webdriver.Firefox()

        try:
            driver.get(fighter_url)
            await asyncio.sleep(1)
            return parse_response(driver, athlete)
        except AssertionError:
            print(f"An error occured locating '{athlete}'. Please check your spelling.")
        finally:
            driver.close()

    results = []
    for a in argv:
        data = await request_athlete(a)
        if data is not None:
            results.append(data)

    return results


async def main(athletes):
    if len(athletes) < 2:
        print("error: not enough arguments specified.")
        exit(1)

    print(await gather_requests(athletes[1:]))


if __name__ == "__main__":
    asyncio.run(main(sys.argv))
