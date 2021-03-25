from django.urls import path, include
from .views import *

from django.conf.urls.static import static

urlpatterns = [
	path('', IndexView.as_view(), name='home'),
	path('search_book/', search_book, name='search_book'),
	path('books/', BookList.as_view(), name='book-list'),
	path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
	path('authors/', AuthorList.as_view(), name='author-list'),
	path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]
