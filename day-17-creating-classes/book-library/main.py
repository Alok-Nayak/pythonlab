from model import Book
from books import books_data

library = []

for book_info in books_data:
    book = Book(book_info["title"], book_info["author"])
    library.append(book)

while True:
    print("\n--- Library Menu ---")
    print("1. View all books")
    print("2. Checkout a book")
    print("3. Return a book")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- List of Books ---")
        for i in range(len(library)):
            book = library[i]
            if book.is_checked_out:
                status = "Checked out"
            else:
                status = "Available"
            print(f"{i+1}. {book.title} by {book.author} | Status: {status}")

    elif choice == "2":
        book_num = int(input("Enter book number to checkout: "))
        if 1 <= book_num <= len(library):
            library[book_num - 1].checkout()
        else:
            print("Invalid book number.")

    elif choice == "3":
        book_num = int(input("Enter book number to return: "))
        if 1 <= book_num <= len(library):
            library[book_num - 1].return_book()
        else:
            print("Invalid book number.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
