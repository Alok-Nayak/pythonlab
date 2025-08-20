class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def checkout(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"'{self.title}' has been checked out.")
        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not checked out.")

    def info(self):
        if self.is_checked_out:
            status = "Checked out"
        else:
            status = "Available"
        print(f"Book: {self.title} by {self.author} | Status: {status}")
