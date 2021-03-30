from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.utils import timezone
from django.db.models import Q

from .models import Book, Author
from .utils import DataMixin, menu


def search_book(request):
	"""
	Запускается, когда пользователь ищет книгу через форму на сайте

	Ищет книгу по ключевому слову (часть названия книги или ее автора) и возвращает список найденных книг
	"""

	search_query = request.GET.get('search', '')

	if search_query:
		books = Book.objects.filter(Q(name__icontains=search_query) | Q(authors__name__icontains=search_query))
	else:
		books = Book.objects.all()

	context = {
	'books': books,
	'search_query': search_query,
	'menu': menu,
	}

	return render(request, 'library/search_book.html', context)


class IndexView(DataMixin, ListView):
	"""
	Отображение главной страницы библиотеки
	"""

	paginate_by = 2
	model = Book
	context_object_name = 'books'
	template_name = 'library/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Библиотека Аладдина')
		context = dict(list(context.items()) + list(c_def.items()))
		return context


class AuthorDetailView(DataMixin, DetailView):
	"""
	Выводит детальную информацию об авторе и списка его книг
	"""

	queryset = Author.objects.all()
	context_object_name = 'author'
	template_name = 'library/author.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Автор: ')
		context = dict(list(context.items()) + list(c_def.items()))
		return context

	def get_object(self):
		"""
		Запоминает, когда этим автором последний раз интересовались
		"""
		obj = super().get_object()
		# Record the last accessed date
		obj.last_accessed = timezone.now()
		obj.save()
		return obj


class AuthorList(DataMixin, ListView):
	"""
	Вывод списка авторов
	"""
	model = Author
	context_object_name = 'authors'
	template_name = 'library/authors.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Все авторы')
		context = dict(list(context.items()) + list(c_def.items()))
		return context


class BookList(DataMixin, ListView):
	"""
	Вывод списка книг
	"""
	paginate_by = 9
	model = Book
	context_object_name = 'books'
	template_name = 'library/books.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Все книги')
		context = dict(list(context.items()) + list(c_def.items()))
		return context

class BookDetailView(DataMixin, DetailView):
	"""
	Вывод детальной информации о книге
	"""
	model = Book
	template_name = 'library/book.html'
	context_object_name = 'book'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		c_def = self.get_user_context(title='Книга:')
		context = dict(list(context.items()) + list(c_def.items()))
		return context
