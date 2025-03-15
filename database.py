import sqlite3

class ChatDatabase:
    def __init__(self, db_name="chat.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, message TEXT, timestamp TEXT)""")
        self.conn.commit()

    def save_message(self, message, timestamp):
        self.cursor.execute("INSERT INTO messages (message, timestamp) VALUES (?, ?)", (message, timestamp))
        self.conn.commit()

    def get_messages(self):
        self.cursor.execute("SELECT * FROM messages")
        return self.cursor.fetchall()
