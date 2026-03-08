# ==============================
# LIBRARY MANAGEMENT SYSTEM
# ==============================
import json
import os

# =========================
# OOP SECTION
# =========================
class Book:
    def __init__(self, title, author, copies=1):
        self.title = title
        self.author = author
        self.copies = copies

    def display(self):
        print(f"Title : {self.title}")
        print(f"Author: {self.author}")
        print(f"Copies: {self.copies}")
        print("-" * 30)


# =========================
# FUNCTION SECTION
# =========================
def load_books():
    if not os.path.exists("library_data.json"):
        return []
    with open("library.json", "r") as file:
        data = json.load(file)
    books = [Book(b["title"], b["author"], b["copies"]) for b in data]
    return books


def save_books(books):
    data = [{"title": b.title, "author": b.author, "copies": b.copies} for b in books]
    with open("library_data.json", "w") as file:
        json.dump(data, file, indent=4)
    print("Library updated!\n")


def add_book(books):
    print("\n=== Add New Book ===")
    title = input("Book Title: ")
    author = input("Author: ")

    # Check if book already exists
    for b in books:
        if b.title.lower() == title.lower() and b.author.lower() == author.lower():
            b.copies += 1
            print("Book already exists. Increased copies by 1.\n")
            return

    book = Book(title, author)
    books.append(book)
    print("Book added successfully!\n")


def view_books(books):
    if not books:
        print("No books in library.\n")
        return
    print("\n=== Library Books ===")
    for b in books:
        b.display()


def search_books(books):
    keyword = input("Enter title or author to search: ").lower()
    found = [b for b in books if keyword in b.title.lower() or keyword in b.author.lower()]
    if not found:
        print("No matching books found.\n")
        return
    print(f"\n=== Found {len(found)} Book(s) ===")
    for b in found:
        b.display()


def borrow_book(books):
    title = input("Enter book title to borrow: ").lower()
    for b in books:
        if b.title.lower() == title:
            if b.copies > 0:
                b.copies -= 1
                print(f"You borrowed '{b.title}' successfully!\n")
            else:
                print("Book not available right now.\n")
            return
    print("Book not found.\n")


def return_book(books):
    title = input("Enter book title to return: ").lower()
    for b in books:
        if b.title.lower() == title:
            b.copies += 1
            print(f"You returned '{b.title}' successfully!\n")
            return
    print("Book not found in library.\n")


# =========================
# MAIN PROGRAM
# =========================
def main():
    books = load_books()

    while True:
        print("\n===== LIBRARY MENU =====")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Select option: ")

        try:
            if choice == "1":
                add_book(books)
                save_books(books)
            elif choice == "2":
                view_books(books)
            elif choice == "3":
                search_books(books)
            elif choice == "4":
                borrow_book(books)
                save_books(books)
            elif choice == "5":
                return_book(books)
                save_books(books)
            elif choice == "6":
                print("Exiting Library Management System...")
                break
            else:
                print("Invalid choice! Try again.\n")
        except Exception as e:
            print("Unexpected error:", e)


if __name__ == "__main__":
    main()