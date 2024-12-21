# OpenFIGHT

This script scrapes fighter stats from the UFC website (use responsibly).

Note that the functionality of this script may change if UFC decides to change up their website. I had to rewrite the scraping code once. As of 11.21.24, the script still works.

## Quickstart

### Dependencies

**OpenFIGHT** has the following dependencies.

* [beautifulsoup4](https://code.launchpad.net/beautifulsoup)
* [prettytable](https://github.com/prettytable/prettytable)
* [requests](https://github.com/psf/requests)

### Installation & Usage

Clone the repository, build a wheel and install with pipx.

The following is an example of a user looking up one fighter.

```
$openfight "Zhang Weili"
Looking up stats for 'Zhang Weili'...
+-------------+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
|             | Wins | Losses | Draws | Total | Fight Win Streak | First Round Finishes | Wins by Knockout | Wins by Submission | Title Defenses |
+-------------+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
| Zhang Weili |  25  |   3    |   0   |   28  |        0         |          11          |        11        |         8          |       0        |
+-------------+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
```

The following is an example of a user attempting to look up multiple fighters at once.

```
$openfight "Alistair Overeem" "Khabib Nurmagomedov" "Daniel Cormier" "Cung Le"
Looking up stats for 'Alistair Overeem'...
Looking up stats for 'Khabib Nurmagomedov'...
Looking up stats for 'Daniel Cormier'...
Looking up stats for 'Cung Le'...
+---------------------+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
|                     | Wins | Losses | Draws | Total | Fight Win Streak | First Round Finishes | Wins by Knockout | Wins by Submission | Title Defenses |
+---------------------+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
|   Alistair Overeem  |  47  |   19   |   0   |   66  |        0         |          0           |        25        |         17         |       0        |
| Khabib Nurmagomedov |  29  |   0    |   0   |   29  |        30        |          0           |        8         |         11         |       0        |
|    Daniel Cormier   |  22  |   3    |   0   |   25  |        0         |          0           |        10        |         5          |       4        |
|       Cung Le       |  9   |   3    |   0   |   12  |        0         |          0           |        0         |         0          |       0        |
+---------------------+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
```
