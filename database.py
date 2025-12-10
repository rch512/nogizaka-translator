import sqlite3

# This will create a file named 'nogizaka.db' in your folder
DB_NAME = "nogizaka.db"


def init_db():
    """Creates the table if it doesn't exist yet."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # We create a table with columns for everything we scraped
    # UNIQUE(url) ensures we never save the same blog twice!
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS blogs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            url TEXT UNIQUE,
            author TEXT,
            title TEXT,
            date TEXT,
            content_jp TEXT,
            content_en TEXT
        )
    """)
    conn.commit()
    conn.close()


def blog_exists(url):
    """Checks if we have already scraped this specific URL."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM blogs WHERE url = ?", (url,))
    result = cursor.fetchone()
    conn.close()
    return result is not None  # Returns True if found, False if new


def save_blog(data):
    """Saves the dictionary of blog data into the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    try:
        cursor.execute("""
            INSERT INTO blogs (url, author, title, date, content_jp, content_en)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            data['url'],
            data['author'],
            data['title'],
            data['date'],
            data['content_jp'],
            data['content_en']
        ))
        conn.commit()
        print(f"✅ Saved to Database: {data['title']}")
    except sqlite3.IntegrityError:
        print(f"⚠️ Skipped (Already exists): {data['title']}")

    conn.close()


if __name__ == "__main__":
    # Run this file once to set up the empty database
    init_db()
    print("Database initialized!")