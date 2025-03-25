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
