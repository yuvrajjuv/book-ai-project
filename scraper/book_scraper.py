import os
import sys
import django
import requests
from bs4 import BeautifulSoup

# 🔥 IMPORTANT: backend path add karo
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BACKEND_DIR = os.path.join(BASE_DIR, 'backend')
sys.path.append(BACKEND_DIR)

# Django setup
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from books.models import Book


def scrape_books():
    url = "http://books.toscrape.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    books = []

    for item in soup.select('.product_pod'):
        title = item.h3.a['title']
        price = item.select_one('.price_color').text.strip()

        books.append({
            "title": title,
            "author": "Unknown",
            "description": price,
            "rating": 0,
            "reviews_count": 0,
            "book_url": url
        })

    return books


def save_books_to_db(books):
    for item in books:
        if not Book.objects.filter(title=item['title']).exists():
            Book.objects.create(
                title=item['title'],
                author=item['author'],
                description=item['description'],
                rating=item['rating'],
                reviews_count=item['reviews_count'],
                book_url=item['book_url']
            )


if __name__ == "__main__":
    data = scrape_books()
    save_books_to_db(data)
    print("Books saved to database!")