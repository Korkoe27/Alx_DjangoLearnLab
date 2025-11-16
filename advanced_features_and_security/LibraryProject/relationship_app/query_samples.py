from relationship_app.models import Author, Book, Library, Librarian


def get_books_by_author(author_name):
    """
    Query all books written by a specific author.
    Args:
        author_name (str): Name of the author
    Returns:
        QuerySet: Books written by the specified author
    """
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return None


def list_library_books(library_name):
    """
    List all books in a specific library.
    Args:
        library_name (str): Name of the library
    Returns:
        QuerySet: Books in the specified library
    """
    try:
        library = Library.objects.get(name=library_name)
        return library.books.all()
    except Library.DoesNotExist:
        return None


def get_library_librarian(library_name):
    """
    Retrieve the librarian for a specific library.
    Args:
        library_name (str): Name of the library
    Returns:
        Librarian: The librarian associated with the library
    """
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        return librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Example usage (optional for manual testing)
if __name__ == "__main__":
    # Query all books by author name
    books = get_books_by_author("J.K. Rowling")
    if books:
        print("Books by J.K. Rowling:")
        for book in books:
            print(f"- {book.title}")
    else:
        print("Author not found.")

    # List all books in a library
    library_books = list_library_books("Central Library")
    if library_books:
        print("\nBooks in Central Library:")
        for book in library_books:
            print(f"- {book.title}")
    else:
        print("\nLibrary not found.")

    # Retrieve the librarian for a library
    librarian = get_library_librarian("Central Library")
    if librarian:
        print(f"\nLibrarian for Central Library: {librarian.name}")
    else:
        print("\nNo librarian found for this library.")
