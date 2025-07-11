from django.contrib import admin
from .models import Book

# Custom admin class
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')   # Columns in list view
    search_fields = ('title', 'author')                      # Search bar functionality
    list_filter = ('publication_year',)   # Filter by publication year
