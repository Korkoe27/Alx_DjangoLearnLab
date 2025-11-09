from django.urls import path
from .views import list_books, LibraryDetailView  # Explicit import as required by ALX

urlpatterns = [
    # Function-based view
    path('books/', list_books, name='list_books'),

    # Class-based view
    path('library/<str:library_name>/', LibraryDetailView.as_view(), name='library_detail'),
]
