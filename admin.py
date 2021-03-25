from django.contrib import admin
from .models import *


class AuthorAdmin(admin.ModelAdmin):
	fields = ['name', 'photo', 'birthdate', 'deathdate']


admin.site.register(Book)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)