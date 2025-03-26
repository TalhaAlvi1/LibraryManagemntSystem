import json

class LibraryManagementSystem:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r") as file:
                self.books = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            self.books = []

    def save_books(self):
        with open(self.filename, "w") as file:
            json.dump(self.books, file, indent=4)

    def add_book(self, title, author, year):
        self.books.append({"title": title, "author": author, "year": year})
        self.save_books()
        print(f"Book '{title}' added successfully!")
     def remove_book(self, title):
        self.books = [book for book in self.books if book["title"].lower() != title.lower()]
        self.save_books()
        print(f"Book '{title}' removed successfully!")

    def display_books(self):
        if not self.books:
            print("No books available in the library.")
        else:
            print("\nLibrary Books:")
            for book in self.books:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")

    def search_book(self, title):
        results = [book for book in self.books if title.lower() in book["title"].lower()]
        if results:
            print("\nSearch Results:")
            for book in results:
                print(f"Title: {book['title']}, Author: {book['author']}, Year: {book['year']}")
        else:
            print("No book found with that title.")
