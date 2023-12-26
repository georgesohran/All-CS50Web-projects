import sqlite3


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")
db = sqlite3.connect(db_path, check_same_thread=False)
cur = db.cursor()


cur.execute("INSERT INTO students (name, password_hash) VALUES ('timmy', 'amongus228eee')")
db.commit()
