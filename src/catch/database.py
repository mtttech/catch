from typing import Any, Dict

import mysql.connector  # pyright: ignore


class _Database:
    def __enter__(self):
        self.db = mysql.connector.connect(
            host="localhost", user="catch", passwd="#Elegrim9162", database="catch"
        )
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb) -> None:
        if exc_type:
            print(f"{exc_type} {exc_value}")
            print(exc_tb)
        if self.db is not None:
            self.db.close()


class InitDB(_Database):
    def __init__(self) -> None:
        super().__init__()

    def create_table(self) -> None:
        table = """ CREATE TABLE IF NOT EXISTS ufcstats (
            Athlete VARCHAR(255) NOT NULL,
            Wins INT(4),
            Losses INT(4),
            Draws INT(4),
            Total INT(4),
            Fight_Win_Streak INT(4),
            Fight_Round_Finishes INT(4),
            Wins_by_Knockout INT(4),
            Wins_by_Submission INT(4),
            Title_Defenses INT(4),
            UNIQUE (Athlete)
        ) ENGINE=InnoDB DEFAULT CHARSET=latin1; """
        self.cursor.execute(table)
        self.db.commit()


class _Record(_Database):
    def __init__(self, data: Dict[str, Any]) -> None:
        super().__init__()
        self.data = tuple(data.values())

    def insert(self) -> int:
        sql = """ INSERT INTO ufcstats (
            Athlete,
            Wins,
            Losses,
            Draws,
            Total,
            Fight_Win_Streak,
            Fight_Round_Finishes,
            Wins_by_Knockout,
            Wins_by_Submission,
            Title_Defenses
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s); """
        self.cursor.execute(sql, self.data)
        self.db.commit()
        return self.cursor.rowcount

    def is_match(self) -> int:
        sql = """ SELECT COUNT(*) FROM ufcstats
            WHERE Athlete = %s
            AND Wins = %s
            AND Losses = %s
            AND Draws = %s
            AND Total = %s
            AND Fight_Win_Streak = %s
            AND Fight_Round_Finishes = %s
            AND Wins_by_Knockout = %s
            AND Wins_by_Submission = %s
            AND Title_Defenses = %s; """
        self.cursor.execute(sql, self.data)
        return self.cursor.fetchone()[0]

    def num_of_rows(self) -> int:
        sql = "SELECT COUNT(*) FROM ufcstats WHERE Athlete = %s;"
        self.cursor.execute(sql, (self.data[0],))
        return self.cursor.fetchone()[0]

    def update(self) -> int:
        athlete = self.data[0]
        data = list(self.data[1:])
        data.append(athlete)
        sql = """ UPDATE ufcstats SET 
                Wins = %s,
                Losses = %s,
                Draws = %s,
                Total = %s,
                Fight_Win_Streak = %s,
                Fight_Round_Finishes = %s,
                Wins_by_Knockout = %s,
                Wins_by_Submission = %s,
                Title_Defenses = %s
            WHERE Athlete = %s; """
        self.cursor.execute(sql, data)
        self.db.commit()
        return self.cursor.rowcount


class Fighter:
    def __init__(self, data: Dict[str, Any]):
        with _Record(data) as record:
            if record.num_of_rows() == 0:
                record.insert()
            else:
                if not record.is_match():
                    record.update()


with InitDB() as db:
    db.create_table()
