import sqlite3


class Database:
    def __enter__(self):
        self.db = sqlite3.connect("catch.db")
        self.cursor = self.db.cursor()
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        if exc_type:
            print(f"{exc_type} {exc_value}")
        if self.db is not None:
            self.db.commit()
            self.db.close()


class InitDB(Database):
    def __init__(self):
        super().__init__()

    def create(self):
        table = """ CREATE TABLE IF NOT EXISTS ufcstats (
            Athlete VARCHAR(255) NOT NULL,
            Wins INT,
            Losses INT,
            Draws INT,
            Total INT,
            Fight_Win_Streak INT,
            Fight_Round_Finishes INT,
            Wins_by_Knockout INT,
            Wins_by_Submission INT,
            Title_Defenses INT
        ); """
        self.cursor.execute(table)


class Base(Database):
    def __init__(self, d):
        super().__init__()
        self.d = d

    def create(self):
        table = """ INSERT INTO ufcstats (
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
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        self.cursor.execute(table, tuple(self.d.values()))
        #print(tuple(self.d.values()))


class Fighter:
    def __init__(self, d):
        with Base(d) as db:
            db.create()


with InitDB() as db:
    db.create()
