"""
Library Management System using Object-Oriented Programming
Features: Add Book, View Books, Search Book, Issue Book, Return Book, Save to File
"""

import os

class Book:
    """Represents a book in the library."""
    def __init__(self, title, author, isbn, status="Available"):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.status = status  # Available or Issued
    
    def __str__(self):
        return f"{self.title},{self.author},{self.isbn},{self.status}"
    
    @classmethod
    def from_string(cls, book_string):
        """Create a Book object from a comma-separated string."""
        parts = book_string.strip().split(",")
        if len(parts) == 4:
            return cls(parts[0], parts[1], parts[2], parts[3])
        return None

class Library:
    """Manages the library collection and operations."""
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()
    
    def load_books(self):
        """Load books from the text file."""
        self.books = []
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    for line in file:
                        if line.strip():
                            book = Book.from_string(line)
                            if book:
                                self.books.append(book)
                print(f"Loaded {len(self.books)} books from {self.filename}")
            except Exception as e:
                print(f"Error loading books: {e}")
        else:
            print(f"No existing file found. Creating new {self.filename}")
            self.save_books()
    
    def save_books(self):
        """Save all books to the text file."""
        try:
            with open(self.filename, "w") as file:
                for book in self.books:
                    file.write(str(book) + "\n")
            print(f"Saved {len(self.books)} books to {self.filename}")
        except Exception as e:
            print(f"Error saving books: {e}")
    
    def add_book(self, title, author, isbn):
        """Add a new book to the library."""
        # Check if ISBN already exists
        for book in self.books:
            if book.isbn == isbn:
                print(f"Error: Book with ISBN {isbn} already exists.")
                return False
        
        new_book = Book(title, author, isbn)
        self.books.append(new_book)
        self.save_books()
        print(f"Book '{title}' added successfully.")
        return True
    
    def view_all_books(self):
        """Display all books in the library."""
        if not self.books:
            print("No books available in the library.")
            return
        
        print("\n" + "="*80)
        print(f"{'Title':<30} {'Author':<25} {'ISBN':<15} {'Status':<10}")
        print("="*80)
        for book in self.books:
            print(f"{book.title:<30} {book.author:<25} {book.isbn:<15} {book.status:<10}")
        print("="*80)
        print(f"Total Books: {len(self.books)}")
    
    def search_book(self, title):
        """Search for a book by title (case-insensitive)."""
        results = [book for book in self.books if title.lower() in book.title.lower()]
        if results:
            print(f"\nFound {len(results)} book(s) matching '{title}':")
            for book in results:
                print(f"  - {book.title} by {book.author} (ISBN: {book.isbn}, Status: {book.status})")
        else:
            print(f"No books found matching '{title}'.")
        return results
    
    def issue_book(self, isbn):
        """Issue a book by changing its status to 'Issued'."""
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "Available":
                    book.status = "Issued"
                    self.save_books()
                    print(f"Book '{book.title}' has been issued successfully.")
                    return True
                else:
                    print(f"Book '{book.title}' is already issued.")
                    return False
        print(f"Book with ISBN {isbn} not found.")
        return False
    
    def return_book(self, isbn):
        """Return a book by changing its status to 'Available'."""
        for book in self.books:
            if book.isbn == isbn:
                if book.status == "Issued":
                    book.status = "Available"
                    self.save_books()
                    print(f"Book '{book.title}' has been returned successfully.")
                    return True
                else:
                    print(f"Book '{book.title}' was not issued.")
                    return False
        print(f"Book with ISBN {isbn} not found.")
        return False

def display_menu():
    """Display the main menu options."""
    print("\n" + "="*50)
    print("       LIBRARY MANAGEMENT SYSTEM")
    print("="*50)
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search Book by Title")
    print("4. Issue a Book")
    print("5. Return a Book")
    print("6. Exit")
    print("="*50)

def get_valid_input(prompt, input_type=str):
    """Get validated input from the user."""
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                print("Input cannot be empty. Please try again.")
                continue
            if input_type == int:
                return int(value)
            return value
        except ValueError:
            print(f"Invalid input. Please enter a valid {input_type.__name__}.")

def main():
    """Main function to run the Library Management System."""
    library = Library("books.txt")
    
    while True:
        display_menu()
        choice = get_valid_input("Enter your choice (1-6): ")
        
        if choice == "1":
            # Add a Book
            print("\n--- Add a New Book ---")
            title = get_valid_input("Enter book title: ")
            author = get_valid_input("Enter author name: ")
            isbn = get_valid_input("Enter ISBN: ")
            library.add_book(title, author, isbn)
        
        elif choice == "2":
            # View All Books
            library.view_all_books()
        
        elif choice == "3":
            # Search Book by Title
            print("\n--- Search Book ---")
            title = get_valid_input("Enter book title to search: ")
            library.search_book(title)
        
        elif choice == "4":
            # Issue a Book
            print("\n--- Issue a Book ---")
            isbn = get_valid_input("Enter ISBN of the book to issue: ")
            library.issue_book(isbn)
        
        elif choice == "5":
            # Return a Book
            print("\n--- Return a Book ---")
            isbn = get_valid_input("Enter ISBN of the book to return: ")
            library.return_book(isbn)
        
        elif choice == "6":
            # Exit
            print("\nThank you for using the Library Management System!")
            print("All data has been saved. Goodbye! 📚")
            break
        
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
