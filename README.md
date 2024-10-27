# OpenFIGHT

This script scrapes fighter stats from the UFC website (use responsibly).

Note that the functionality of this script may change if UFC decides to change up their website. I had to rewrite the scraping code once. As of 01.13.24, the script still works.

## Quickstart

### Dependencies

**OpenFIGHT** has the following dependencies.

* [selenium](https://github.com/SeleniumHQ/selenium)

### Installation & Usage

Clone the repository and change into its directory.

```
git clone https://codeberg.com/mtttech/openfight.git
cd openfight
```

The following is an example of a user looking up one fighter.

```
$poetry run python openfight.py "Zhang Weili"
Looking up (Zhang Weili @ https://www.ufc.com/athlete/zhang-weili)...
Stats found for Zhang Weili.
[{'athlete': 'Zhang Weili', 'wins': 24, 'losses': 3, 'draws': 0, 'total': 27, 'fight_win_streak': 0, 'first_round_finishes': 11, 'wins_by_knockout': 11, 'wins_by_submission': 8, 'title_defenses': 0}]
```

The following is an example of a user attempting to look up multiple fighters at once.

```
$poetry run python openfight.py "Alistair Overeem" "Khabib Nurmagomedov" "Daniel Cormier" "Cung Le"
Looking up (Alistair Overeem @ https://www.ufc.com/athlete/alistair-overeem)...
Looking up (Khabib Nurmagomedov @ https://www.ufc.com/athlete/khabib-nurmagomedov)...
Looking up (Daniel Cormier @ https://www.ufc.com/athlete/daniel-cormier)...
Looking up (Cung Le @ https://www.ufc.com/athlete/cung-le)...
Stats found for Alistair Overeem.
Stats found for Khabib Nurmagomedov.
Stats found for Daniel Cormier.
Stats found for Cung Le.
[{'athlete': 'Alistair Overeem', 'wins': 47, 'losses': 19, 'draws': 0, 'total': 66, 'fight_win_streak': 0, 'first_round_finishes': 0, 'wins_by_knockout': 25, 'wins_by_submission': 17, 'title_defenses': 0}, {'athlete': 'Khabib Nurmagomedov', 'wins': 29, 'losses': 0, 'draws': 0, 'total': 29, 'fight_win_streak': 30, 'first_round_finishes': 0, 'wins_by_knockout': 8, 'wins_by_submission': 11, 'title_defenses': 0}, {'athlete': 'Daniel Cormier', 'wins': 22, 'losses': 3, 'draws': 0, 'total': 25, 'fight_win_streak': 0, 'first_round_finishes': 0, 'wins_by_knockout': 10, 'wins_by_submission': 5, 'title_defenses': 4}, {'athlete': 'Cung Le', 'wins': 9, 'losses': 3, 'draws': 0, 'total': 12, 'fight_win_streak': 0, 'first_round_finishes': 0, 'wins_by_knockout': 0, 'wins_by_submission': 0, 'title_defenses': 0}]
```
