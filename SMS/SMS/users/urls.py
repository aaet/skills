from django.urls import path
from .views import *

urlpatterns = [
    path('', index_users),
    path('technical_support/', technical_support),
    path('solution_managers/', solution_managers),
]