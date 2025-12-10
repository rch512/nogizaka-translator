import requests
from bs4 import BeautifulSoup


def scrape_blog(url):
    """
    Visits a Nogizaka46 blog URL and extracts metadata + body.
    Returns: A dictionary with title, author, date, and content.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # 1. Extract Metadata (using the tags you found!)
    # We use .text.strip() to remove whitespace
    title = soup.find("h1", class_="bd--hd__ttl").text.strip()
    author = soup.find("p", class_="bd--prof__name").text.strip()
    date = soup.find("p", class_="bd--hd__date").text.strip()

    # 2. Extract Body
    blog_body = soup.find("div", class_="bd--edit")

    if blog_body:
        content = blog_body.get_text("\n", strip=True)
    else:
        content = "Error: Content not found"

    # 3. Return everything as a dictionary
    return {
        "url": url,
        "title": title,
        "author": author,
        "date": date,
        "content_jp": content
    }


if __name__ == "__main__":
    # Test with a real URL
    test_url = "https://www.nogizaka46.com/s/n46/diary/detail/102946?ima=0000"
    data = scrape_blog(test_url)

    print(f"Title:  {data['title']}")
    print(f"Author: {data['author']}")
    print(f"Date:   {data['date']}")
    print("-" * 20)
    print(f"Body Start: {data['content_jp'][:100]}...")