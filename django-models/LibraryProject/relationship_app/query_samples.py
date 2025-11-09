from django.db import models
from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_id):
    """
    Query all books written by a specific author
    Args:
        author_id: ID of the author
    Returns:
        QuerySet of books by the specified author
    """
    try:
        # Get all books by the author using the related name
        books = Book.objects.filter(author_id=author_id)
        return books
    except Author.DoesNotExist:
        return None

def list_library_books(library_id):
    """
    List all books in a specific library
    Args:
        library_id: ID of the library
    Returns:
        QuerySet of all books in the specified library
    """
    try:
        # Get all books in the library
        library = Library.objects.get(id=library_id)
        books = library.books.all()  # Assuming there's a related_name='books' in the Book model
        return books
    except Library.DoesNotExist:
        return None

def get_library_librarian(library_id):
    """
    Retrieve the librarian for a specific library
    Args:
        library_id: ID of the library
    Returns:
        Librarian object associated with the library
    """
    try:
        # Get the librarian of the library (assuming one-to-one relationship)
        library = Library.objects.get(id=library_id)
        return library.librarian  # Assuming there's a OneToOne relationship with Librarian
    except Library.DoesNotExist:
        return None

# Example usage:
if __name__ == "__main__":
    # Example: Get all books by author with ID 1
    author_books = get_books_by_author(1)
    if author_books:
        print("Books by author:")
        for book in author_books:
            print(f"- {book.title}")

    # Example: List all books in library with ID 1
    library_books = list_library_books(1)
    if library_books:
        print("\nBooks in library:")
        for book in library_books:
            print(f"- {book.title}")

    # Example: Get librarian for library with ID 1
    librarian = get_library_librarian(1)
    if librarian:
        print(f"\nLibrarian: {librarian.name}")