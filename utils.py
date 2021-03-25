from .models import *

menu = [{'title': "О сайте", 'url': '/'},
		{'title': "Книги", 'url': '/books/'},
		{'title': "Авторы", 'url': '/authors/'},
]

class DataMixin:
	"""
	Миксин для передаче в шаблон списка элементов навбара и текущего url-адреса
	"""

	def get_user_context(self, **kwargs):
		context = kwargs
		context['menu'] = menu.copy()
		context['activeurl'] = self.request.get_full_path
		return context
