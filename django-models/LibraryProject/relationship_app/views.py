from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from .models import Book
from .models import Library

# Function-Based View: List all books
def list_books(request):
    books = Book.objects.all()
    # Use the full path relative to the templates folder
    return render(request, 'relationship_app/list_books.html', {'books': books})


# Class-Based View: Display details of a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_object(self):
        library_name = self.kwargs.get('library_name')
        return get_object_or_404(Library, name=library_name)
