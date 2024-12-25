# Catch

**Catch** fighter is webscrapper that rips stats for athletes from the UFC (use responsibly).

*NOTE:* The functionality of this script may change if UFC decides to change up the design of their website. I had to rewrite it once. As of 12.24.24, it still works.

## Quickstart

### Dependencies

**Catch** has the following dependencies.

* [beautifulsoup4](https://code.launchpad.net/beautifulsoup)
* [prettytable](https://github.com/prettytable/prettytable)
* [requests](https://github.com/psf/requests)

### Installation & Usage

Clone the repository, build a wheel and install with pipx.

The following is an example of a user looking up one fighter.

```
$catch "Ailin Perez"
Looking up Ailin Perez...
Stats found for 'Ailin Perez'.
+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
| Wins | Losses | Draws | Total | Fight Win Streak | First Round Finishes | Wins by Knockout | Wins by Submission | Title Defenses |
+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
|  11  |   2    |   0   |   13  |        0         |          5           |        4         |         2          |       0        |
+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
```

The following is an example of a user looking up multiple fighters.

```
$catch "Alistair Overeem" "Daniel Cormier"
Looking up stats for 'Alistair Overeem'...
Stats found for 'Alistair Overeem'.
+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
| Wins | Losses | Draws | Total | Fight Win Streak | First Round Finishes | Wins by Knockout | Wins by Submission | Title Defenses |
+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
|  47  |   19   |   0   |   66  |        0         |          0           |        25        |         17         |       0        |
+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
Looking up stats for 'Daniel Cormier'...
Stats found for 'Daniel Cormier'.
+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
| Wins | Losses | Draws | Total | Fight Win Streak | First Round Finishes | Wins by Knockout | Wins by Submission | Title Defenses |
+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
|  22  |   3    |   0   |   25  |        0         |          0           |        10        |         5          |       4        |
+------+--------+-------+-------+------------------+----------------------+------------------+--------------------+----------------+
```
