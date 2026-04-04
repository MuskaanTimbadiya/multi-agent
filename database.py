import sqlite3

conn = sqlite3.connect("data.db", check_same_thread=False)
cursor = conn.cursor()

# Create tables
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    event TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    note TEXT
)
""")

conn.commit()

def insert_task(task):
    cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
    conn.commit()

def get_tasks():
    cursor.execute("SELECT task FROM tasks")
    return cursor.fetchall()

def insert_event(event):
    cursor.execute("INSERT INTO events (event) VALUES (?)", (event,))
    conn.commit()

def get_events():
    cursor.execute("SELECT event FROM events")
    return cursor.fetchall()

def insert_note(note):
    cursor.execute("INSERT INTO notes (note) VALUES (?)", (note,))
    conn.commit()

def get_notes():
    cursor.execute("SELECT note FROM notes")
    return cursor.fetchall()

# DELETE TASK
def delete_task(task):
    cursor.execute("DELETE FROM tasks WHERE task LIKE ?", ('%' + task + '%',))
    conn.commit()

# DELETE EVENT
def delete_event(event):
    cursor.execute("DELETE FROM events WHERE event LIKE ?", ('%' + event + '%',))
    conn.commit()

# DELETE NOTE
def delete_note(note):
    cursor.execute("DELETE FROM notes WHERE note LIKE ?", ('%' + note + '%',))
    conn.commit()
