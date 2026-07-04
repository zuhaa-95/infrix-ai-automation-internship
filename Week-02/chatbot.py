import json
import os

def load_books():
    with open('books.json', 'r') as f:
        return json.load(f)

def find_books(query, books):
    query = query.lower()
    results = []
    
    for book in books:
        if query in book['title'].lower():
            results.append(book)
    
    return results

def chatbot():
    books = load_books()
    print("📚 Book Chatbot Ready!")
    print("Ask me about any book, price or rating!")
    print("Type 'quit' to exit\n")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        if 'cheap' in user_input.lower() or 'affordable' in user_input.lower():
            cheap_books = sorted(books, key=lambda x: x['price'])[:5]
            print("\nCheapest books:")
            for book in cheap_books:
                print(f"- {book['title']} | {book['price']}")
        
        elif 'expensive' in user_input.lower():
            expensive_books = sorted(books, key=lambda x: x['price'], reverse=True)[:5]
            print("\nMost expensive books:")
            for book in expensive_books:
                print(f"- {book['title']} | {book['price']}")
        
        elif 'how many' in user_input.lower():
            print(f"\nWe have {len(books)} books in total!")
        
        else:
            results = find_books(user_input, books)
            if results:
                print(f"\nFound {len(results)} book(s):")
                for book in results:
                    print(f"- {book['title']} | {book['price']} | Rating: {book['rating']}")
            else:
                print("\nNo books found! Try another search.")
        
        print()

chatbot()