from scraper import scrape_blog
from translator import translate_blog
from database import init_db, blog_exists, save_blog


def run_pipeline():
    # 1. Make sure DB is ready
    init_db()

    # Use the URL you were testing with
    target_url = "https://www.nogizaka46.com/s/n46/diary/detail/102946?ima=0000"

    print(f"Checking URL: {target_url}")

    # 2. CHECK: Do we already have this?
    if blog_exists(target_url):
        print("⏭️  We already have this blog in the database. Skipping translation.")
        return  # Stop here, don't waste API credits

    # 3. SCRAPE
    print("📥 Scraping new blog...")
    blog_data = scrape_blog(target_url)

    if "Error" in blog_data.get('content_jp', ''):
        print("❌ Scrape failed.")
        return

    # 4. TRANSLATE
    print("🤖 Translating...")
    blog_data['content_en'] = translate_blog(blog_data['content_jp'], blog_data['author'])

    # 5. SAVE
    save_blog(blog_data)
    print("🎉 Done! Data is safe in nogizaka.db")


if __name__ == "__main__":
    run_pipeline()