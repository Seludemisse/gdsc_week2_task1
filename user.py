class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.books_borrowed = []

    def display_details(self):
        print("User Details:")
        print(f"User ID: {self.user_id}")
        print(f"Name: {self.name}")
        print("Books Borrowed:", ', '.join(self.books_borrowed))

    def borrow_book(self, book):
        if book.availability_status:
            self.books_borrowed.append(book.title)
            book.update_availability_status(False)
            print(f"{self.name} has successfully borrowed {book.title}")
        else:
            print(f"Sorry, {book.title} is not available for borrowing.")

    def return_book(self, book):
        if book.title in self.books_borrowed:
            self.books_borrowed.remove(book.title)
            book.update_availability_status(True)
            print(f"{self.name} has successfully returned {book.title}")
        else:
            print(f"Sorry, {self.name} does not have {book.title} borrowed.")