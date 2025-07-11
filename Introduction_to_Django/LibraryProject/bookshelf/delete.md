# --- DELETE ---
retrieved_book.delete()
# Output: (1, {'yourapp.Book': 1})  ← number of records deleted
# --- CONFIRM DELETION ---
Book.objects.all()
# Output: <QuerySet []>