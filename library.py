class Library:
    def _init_(self, book_name, author):
        self.book_name = book_name
        self.author = author
        self.is_available = True

    def check_out(self):
        if self.is_available:
            self.is_available = False
            print(f"You have successfully borrowed '{self.book_name}'.")
        else:
            print(f"Sorry, '{self.book_name}' is currently not available.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Thank you for returning '{self.book_name}'.")
        else:
            print(f"'{self.book_name}' was not issued.")

    def display_book(self):
        status = "Available" if self.is_available else "Not Available"
        print("\nBook Details")
        print(f"Name   : {self.book_name}")
        print(f"Author : {self.author}")
        print(f"Status : {status}")
        print("-" * 30)

