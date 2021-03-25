from django.db import models


class Book(models.Model):
	name = models.CharField(max_length=200, verbose_name='Название')
	cover = models.ImageField(blank=True, null=True,upload_to='covers/%Y/%m/%d/', verbose_name='Обложка')
	description = models.TextField(blank=True, null=True, verbose_name='Краткое описание')
	authors = models.ManyToManyField('Author', blank=True, verbose_name='Автор')
	categories = models.ManyToManyField('Category', blank=True, verbose_name='Категория')

	class Meta:
		ordering = ['name']
		verbose_name = 'Книга'
		verbose_name_plural = 'Книги'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f'/books/{self.id}/'


class Author(models.Model):
	name = models.CharField(max_length=200, verbose_name='Имя и фамилия')
	birthdate = models.DateField(null=True, blank=True, verbose_name='Дата рождения')
	deathdate = models.DateField(null=True, blank=True, verbose_name='Дата смерти')
	photo = models.ImageField(verbose_name='Фотография', upload_to='author_photos/%Y/%m/%d/', blank=True, null=True)
	last_accessed = models.DateTimeField(null=True, blank=True, verbose_name='Когда последний раз интересовались автором')

	class Meta:
		ordering = ['name']
		verbose_name = 'Автор'
		verbose_name_plural = 'Авторы'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return f'/authors/{self.id}/'

	@property
	def get_author_books(self):
		"""
		Возвращает все объекты-книги, принадлежащие этому автору
		"""
		return self.book_set.all()


class Category(models.Model):
	"""
	Класс отвечает за категорию книг
	"""
	name = models.CharField(max_length=250, verbose_name='Название')

	class Meta:
		ordering = ['name']
		verbose_name = 'Категория'
		verbose_name_plural = 'Категории'

	def __str__(self):
		return self.name

