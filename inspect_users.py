import sqlite3

DB_PATH = "recipes.db"


def main():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    rows = cur.execute("SELECT id, username, password_hash FROM users").fetchall()

    for row in rows:
        print("id:", row["id"])
        print("username:", row["username"])
        print("password_hash:", row["password_hash"])
        print("-" * 40)

    conn.close()


if __name__ == "__main__":
    main()