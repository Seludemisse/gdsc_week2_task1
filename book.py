class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.availability_status = True

    def display_details(self):
        print("Book Details:")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"ISBN: {self.isbn}")
        print("Availability: Available" if self.availability_status else "Availability: Not Available")

    def update_availability_status(self, status):
        self.availability_status = status

