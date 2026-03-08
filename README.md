Library Management System (Python)
Overview

The Library Management System is a Python console-based application that allows users to manage books in a library. The system supports adding books, searching books, borrowing books, returning books, and viewing the entire library collection.

This project demonstrates important Python programming concepts such as:

Object-Oriented Programming (OOP)

File Handling using JSON

Functions and Modular Programming

Loops and Menu Driven Interface

Exception Handling

Data Persistence

The library data is stored in a JSON file so that information is preserved even after the program is closed.

Features
1. Add Book

Users can add a new book by providing:

Book Title

Author Name

If the book already exists in the library, the system increases the number of copies instead of creating a duplicate entry.

2. View All Books

Displays the list of all books currently available in the library along with:

Title

Author

Number of Copies

3. Search Books

Users can search for books using:

Book title

Author name

The system will display all matching books.

4. Borrow Book

Users can borrow a book by entering its title.

If copies are available:

The system decreases the number of copies by 1

If no copies are available:

A message is displayed that the book is unavailable.

5. Return Book

Users can return a borrowed book.

When a book is returned:

The number of copies increases by 1