import sqlite3
from pathlib import Path

source_path = Path(__file__).resolve()
source_dir = source_path.parent

class RoutineDatabase:

    def __init__(self) -> None:
        self.db_path = source_dir / 'light-routines.db'
        self.conn = None

    def __del__(self):
        if self.conn is not None:
            self.conn.close()

    def connect(self):
        # Create a connection object that represents the database file
        db_path_str = str(self.db_path)
        # if not self.db_path.exists():
        #     self.db_path.touch()
        self.conn = sqlite3.connect(db_path_str)
        # Create a cursor object that allows you to execute SQL commands on the database
        self.cur = self.conn.cursor()

    def create_schema(self):
        # Create a table in the database that can store your key-value pairs
        self.cur.execute('CREATE TABLE IF NOT EXISTS data (name TEXT, data TEXT)')

    def add_routine(self, routine_name, routine_data):
        self.cur.execute('INSERT INTO data VALUES (?, ?)', (routine_name, routine_data))
        # In raw SQL it would look like this
        # INSERT INTO data (name, data) VALUES ('run1', 'color_value_other_stuff spaces')

        # Commit the changes to the database
        self.conn.commit()

    def get_routine(self, routine_name) -> dict:
        # Retrieve your key-value pairs from the table
        self.cur.execute('SELECT * FROM data WHERE name = ?', (routine_name))
        result = self.cur.fetchone()
        return result
