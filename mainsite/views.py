""" Views for mainsite """
from datetime import datetime
from django.shortcuts import render
from .models import Article

def index(request):
    """ handler for main page """
    context = {
        'current_date':datetime.now(),
        'title':'Home'
    }
    return render(request, 'index.html', context)

def about(request):
    """ handler for about page """
    context = {
        'current_date':datetime.now(),
        'title':'About'
    }
    return render(request, 'about.html', context)

def news(request):
    """ handler for news page """
    populate_db()
    articles = get_articles()

    context = {
        'articles':articles,
        'current_date':datetime.now(),
        'title':'News'
    }
    return render(request, 'news.html', context)

def get_articles():
    """ Acquiring the content of the database """
    result = Article.objects.all()
    return result

def populate_db():
    """ Populate empty database """
    if Article.objects.count() == 0:
        Article(title='first item', content='this is the first db item').save()
        Article(title='second item', content='this is the second db item').save()
        Article(title='third item', content='this is the third db item').save()
