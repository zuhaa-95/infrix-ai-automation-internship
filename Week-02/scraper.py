import requests
from bs4 import BeautifulSoup
import json

def scrape_books():
    books = []
    
    for page in range(1, 6):
        url = f"http://books.toscrape.com/catalogue/page-{page}.html"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        for book in soup.select('article.product_pod'):
            title = book.h3.a['title']
            price = book.select_one('p.price_color').text.strip()
            rating = book.p['class'][1]
            
            books.append({
                'title': title,
                'price': price,
                'rating': rating
            })
    
    with open('books.json', 'w') as f:
        json.dump(books, f, indent=2)
    
    print(f"Scraped {len(books)} books successfully!")
    return books

scrape_books()