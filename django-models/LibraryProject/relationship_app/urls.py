from django.urls import path
from .views import list_books, LibraryDetailView
from django.contrib import admin
from django.urls import include

urlpatterns = [
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('admin/', admin.site.urls),
    path('relationships/', include('relationship_app.urls')),
]