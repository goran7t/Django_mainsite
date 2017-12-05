""" admin page for mainsite """
from django.contrib import admin
from .models import Article

admin.site.register(Article)
