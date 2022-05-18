from django.shortcuts import render
from django.http import HttpResponse

from .models import News


def index(request):
    news = News.objects.all()
    content = {
        'news': news,
        'title': 'Список новостей'
    }
    return render(request, 'news/index.html', content)


