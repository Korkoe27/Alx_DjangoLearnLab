from relationship_app.models import Author, Book, Library, Librarian


def get_books_by_author(author_id):
    """
    Query all books written by a specific author.
    Args:
        author_id (int): ID of the author
    Returns:
        QuerySet: Books written by the specified author
    """
    return Book.objects.filter(author_id=author_id)


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


def get_library_librarian(library_id):
    """
    Retrieve the librarian for a specific library.
    Args:
        library_id (int): ID of the library
    Returns:
        Librarian: The librarian associated with the library
    """
    try:
        library = Library.objects.get(id=library_id)
        return library.librarian
    except (Library.DoesNotExist, Librarian.DoesNotExist):
        return None


# Optional examples for testing
if __name__ == "__main__":
    # Query all books by author with ID 1
    books = get_books_by_author(1)
    print("Books by Author (ID=1):")
    for book in books:
        print(f"- {book.title}")

    # List all books in a library named "Central Library"
    library_books = list_library_books("Central Library")
    if library_books:
        print("\nBooks in Central Library:")
        for book in library_books:
            print(f"- {book.title}")
    else:
        print("\nLibrary not found.")

    # Retrieve the librarian for library with ID 1
    librarian = get_library_librarian(1)
    if librarian:
        print(f"\nLibrarian for Library ID 1: {librarian.name}")
    else:
        print("\nNo librarian found for this library.")
