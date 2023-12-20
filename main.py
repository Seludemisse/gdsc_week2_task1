from library import Library
from transaction import Transaction
from book import Book
from user import User


def display_menu():
    print("------ Library Management System ------")
    print("1. Add Book")
    print("2. Register User")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Display All Users")
    print("7. Generate Transaction Report")
    print("8. Exit")


def main():
    library = Library()
    transaction = Transaction()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter the title of the book: ")
            author = input("Enter the author of the book: ")
            isbn = input("Enter the ISBN of the book: ")
            book = Book(title, author, isbn)
            library.add_book(book)

        elif choice == '2':
            user_id = input("Enter the user ID: ")
            name = input("Enter the name of the user: ")
            user = User(user_id, name)
            library.register_user(user)

        elif choice == '3':
            user_id = input("Enter the user ID: ")
            book_title = input("Enter the title of the book to borrow: ")
            user = library.find_user_by_id(user_id)
            book = library.find_book_by_title(book_title)

            if user and book:
                user.borrow_book(book)
                transaction.record_transaction(user, book, "Borrowed")
            else:
                print("Invalid user ID or book title.")

        elif choice == '4':
            user_id = input("Enter the user ID: ")
            book_title = input("Enter the title of the book to return: ")
            user = library.find_user_by_id(user_id)
            book = library.find_book_by_title(book_title)

            if user and book:
                user.return_book(book)
                transaction.record_transaction(user, book, "Returned")
            else:
                print("Invalid user ID or book title.")

        elif choice == '5':
            library.display_all_books()

        elif choice == '6':
            library.display_all_users()

        elif choice == '7':
            transaction.generate_transaction_report()

        elif choice == '8':
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

        print()


if __name__ == "__main__":
    main()