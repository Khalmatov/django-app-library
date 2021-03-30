from django.urls import path, include
from django.conf import settings
from .views import *

from django.conf.urls.static import static
import debug_toolbar

urlpatterns = [
	path('', IndexView.as_view(), name='home'),
	path('search_book/', search_book, name='search_book'),
	path('books/', BookList.as_view(), name='book-list'),
	path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
	path('authors/', AuthorList.as_view(), name='author-list'),
	path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]

if settings.DEBUG:
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)