import sqlite3
from auth_utils import hash_password

DB_PATH = "recipes.db"


def create_user(username: str, plain_password: str) -> None:
    password_hash = hash_password(plain_password)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute(
        """
        INSERT INTO users (username, password_hash)
        VALUES (?, ?)
        """,
        (username, password_hash),
    )

    conn.commit()
    conn.close()

    print(f"Created user '{username}' with a hashed password.")


def main():
    # CHANGE THESE TO FAKE TEST VALUES ONLY
    username = "testuser"
    plain_password = "test-password-123"

    create_user(username, plain_password)


if __name__ == "__main__":
    main()