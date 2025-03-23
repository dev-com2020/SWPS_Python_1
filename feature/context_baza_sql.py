import sqlite3
from contextlib import contextmanager
from typing import Iterator


@contextmanager
def db_cursor(db_path: str) -> Iterator[sqlite3.Cursor]:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    try:
        yield cursor
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"Błąd: {e}, wykonano rollback")
        raise
    finally:
        cursor.close()
        conn.close()

with db_cursor("test.db") as cur:
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO users (name) VALUES (?)", ("Tomek",))
