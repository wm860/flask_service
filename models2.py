import sqlite3


class Db_start:
    def __init__(self):
        self.conn = sqlite3.connect("poll.db")
        self.c = self.conn.cursor()
        self.create_user_table()
        self.create_poll_table()

    def create_poll_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS poll (
            id INTEGER PRIMARY KEY,
            username TEXT,
            age INTEGER,
            city TEXT,
            country TEXT
            UserId INTEGER 
            FOREIGNKEY(UserID) REFERENCES user(id)
        );
        """
        self.c.execute(query)
        self.conn.commit()

    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "user" (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        );
        """
        self.c.execute(query)
        self.conn.commit()


class PollModel:
    def __init__(self):
        self.conn = sqlite3.connect("poll.db")
        self.c = self.conn.cursor()

    def add_record(self, username, age, city, country):
        self.c.execute(
            "INSERT INTO poll (username, age, city, country) VALUES (?, ?, ?, ?)",
            (username, age, city, country),
        )
        # self.c.execute('INSERT INTO user (username) VALUES (?, 1234)', (username,))
        self.conn.commit()
        return self.c.lastrowid

    def get_records(self):
        self.c.execute("SELECT * FROM poll")
        return self.c.fetchall()

    def close(self):
        self.conn.close()


class Db_service:
    def __init__(self):
        self.model = PollModel()

    def add_record_to_poll(self, username, age, city, country):
        return self.model.add_record(username, age, city, country)
