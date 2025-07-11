# --- Import the model ---
from bookshelf.models import Book

# --- CREATE ---
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output:
# 1984 by George Orwell (1949)

# --- RETRIEVE ---
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title)           # Output: 1984
print(retrieved_book.author)          # Output: George Orwell
print(retrieved_book.publication_year) # Output: 1949

# --- UPDATE ---
retrieved_book.title = "Nineteen Eighty-Four"
retrieved_book.save()
print(retrieved_book.title)
# Output: Nineteen Eighty-Four

# --- DELETE ---
retrieved_book.delete()
# Output: (1, {'bookshelf.Book': 1})  ← number of records deleted

# --- CONFIRM DELETION ---
Book.objects.all()
# Output: <QuerySet []>
