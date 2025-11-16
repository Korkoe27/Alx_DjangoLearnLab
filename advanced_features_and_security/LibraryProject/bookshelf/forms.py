from django import forms
from .models import Book

class ExampleForm(forms.ModelForm):
    """
    Example form to demonstrate secure form handling in Django.
    - Uses ModelForm to safely map fields to the Book model.
    - Validates input to prevent malicious data.
    - Safe for CSRF-protected templates.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter book title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter author name'}),
            'published_date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }

    # Example of additional validation
    def clean_title(self):
        title = self.cleaned_data.get('title')
        if "<script>" in title.lower():  # basic XSS prevention
            raise forms.ValidationError("Invalid characters in title")
        return title