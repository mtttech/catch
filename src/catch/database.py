import mysql.connector
from typing import Any, Dict


class Database:
    def __enter__(self):
        self.db = mysql.connector.connect(
            host="localhost", user="catch", passwd="#Elegrim9162", database="catch"
        )
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            print(f"{exc_type} {exc_value}")
            print(exc_tb)
        if self.db is not None:
            self.db.close()


class InitDB(Database):
    def __init__(self):
        super().__init__()

    def create_table(self):
        table = """ CREATE TABLE IF NOT EXISTS ufcstats (
            Athlete VARCHAR(255) NOT NULL,
            Wins INT(11),
            Losses INT(11),
            Draws INT(11),
            Total INT(11),
            Fight_Win_Streak INT(11),
            Fight_Round_Finishes INT(11),
            Wins_by_Knockout INT(11),
            Wins_by_Submission INT(11),
            Title_Defenses INT(11),
            UNIQUE (Athlete)
        ); """
        self.cursor.execute(table)
        self.db.commit()


class _Record(Database):
    def __init__(self, data: Dict[str, Any]):
        super().__init__()
        self.data = data

    def insert(self):
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
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"""
        self.cursor.execute(sql, tuple(self.data.values()))
        self.db.commit()


class Fighter:
    def __init__(self, data: Dict[str, Any]):
        with _Record(data) as record:
            record.insert()


with InitDB() as db:
    db.create_table()
