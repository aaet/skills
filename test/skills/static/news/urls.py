from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from news.views import *

urlpatterns = [
    path('', index, name='home'),
    path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:news_id>/', view_news, name='view_news'),
]