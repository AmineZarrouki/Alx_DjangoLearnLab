from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    return Book.objects.filter(author=author)

def get_books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()

def get_librarian_for_library(library_name):
    library = Library.objects.get(name=library_name)
    return Librarian.objects.get(library=library)  # Exact requested pattern

# Alternative implementations
def get_librarian_for_library_direct(library_name):
    return Librarian.objects.get(library__name=library_name)

def get_libraries_with_book(book_title):
    return Library.objects.filter(books__title=book_title)