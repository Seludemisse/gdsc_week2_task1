
class Library:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book):
        self.books.append(book)
        print(f"{book.title} has been added to the library.")

    def register_user(self, user):
        self.users.append(user)
        print(f"{user.name} has been registered as a library user.")

    def find_book_by_title(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def find_user_by_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def display_all_books(self):
        print("All Books in Library:")
        for book in self.books:
            book.display_details()

    def display_all_users(self):
        print("All Registered Users:")
        for user in self.users:
            user.display_details()

