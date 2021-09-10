import sqlite3
from dataclasses import dataclass

class Note:
    def __init__(self, id=None, title=None, content=''):
        self.id = id
        self.title = title
        self.content = content

class Database():

    def __init__(self, name):
        self.name = f'{name}.db'
        self.conn = sqlite3.connect(self.name)
        self.note = self.conn.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY, title STRING, content STRING NOT NULL);")

    def add(self, note):
        self.conn.execute("INSERT INTO note (title, content) VALUES (?, ?);", (note.title, note.content))
        self.conn.commit()

    def get_all(self):
        noteList = []
        notes = self.conn.execute("SELECT id, title, content FROM note")
        for note in notes:
            noteList.append(Note(id = note[0], title=note[1], content=note[2]))
        return noteList

    def update(self, entry):
        self.conn.execute("UPDATE note SET title = ? WHERE id = ?", (entry.title, entry.id))
        self.conn.commit()
        self.conn.execute("UPDATE note SET content = ? WHERE id = ?", (entry.content, entry.id))
        self.conn.commit()

    def delete(self, note_id):
        self.conn.execute("DELETE FROM note WHERE id = ?", (str(note_id)))
        self.conn.commit()