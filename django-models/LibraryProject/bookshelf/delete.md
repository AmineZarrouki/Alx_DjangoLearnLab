# --- DELETE ---
from bookshelf.models import Book
retrieved_book.delete()
# Output: (1, {'bookshelf.Book': 1})  ← number of records deleted
# --- CONFIRM DELETION ---
Book.objects.all()
# Output: <QuerySet []>