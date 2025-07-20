from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library  # Explicit import of Library as requested

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})

# Class-based view to display library details and books
class LibraryDetailView(DetailView):
    model = Library  # Using the imported Library model
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Get all books for this library
        context['books'] = self.object.books.all()  
        return context