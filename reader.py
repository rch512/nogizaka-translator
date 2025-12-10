import sqlite3

DB_NAME = "nogizaka.db"


def view_all_blogs():
    """
    Connects to the database and prints all saved blogs.
    """
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # SQL QUERY:
    # SELECT * -> Give me every column
    # FROM blogs         -> From the 'blogs' table
    # ORDER BY date DESC -> Show me the newest ones first
    cursor.execute("SELECT title, author, date, content_en FROM blogs ORDER BY date DESC")

    # fetchall() grabs every single row found by the query
    rows = cursor.fetchall()

    print(f"\n📚 Found {len(rows)} blogs in the database:\n")

    for row in rows:
        # row is a tuple: (title, author, date, content_en)
        title = row[0]
        author = row[1]
        date = row[2]
        content_summary = row[3][:100] + "..."  # First 100 chars only

        print(f"🎤 {author} ({date})")
        print(f"   Title: {title}")
        print(f"   Preview: {content_summary}")
        print("-" * 40)

    conn.close()


if __name__ == "__main__":
    view_all_blogs()