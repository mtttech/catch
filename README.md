# Catch

**Catch** is a script that scrapes fighter stats from the UFC website (use responsibly).

*NOTE:* The functionality of this script may change if UFC decides to change up the design of their website. I had to rewrite it once. As of 06.07.25, it still works.

## Quickstart

### Dependencies

**Catch** has the following dependencies.

* [beautifulsoup4](https://code.launchpad.net/beautifulsoup)
* [mysql-connector](https://github.com/mysql/mysql-connector-python)
* [prettytable](https://github.com/prettytable/prettytable)
* [requests](https://github.com/psf/requests)

### Installation & Usage

Clone the repository, build a wheel and install with pipx.

The following is the command to look up one fighter.

```
$catch "Ailin Perez"
```

The following is the command to look up multiple fighters.

```
$catch "Alistair Overeem" "Daniel Cormier"
```
