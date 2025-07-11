# --- RETRIEVE ---
retrieved_book = Book.objects.get(title="1984")
print(retrieved_book.title)           # Output: 1984
print(retrieved_book.author)          # Output: George Orwell
print(retrieved_book.publication_year) # Output: 1949