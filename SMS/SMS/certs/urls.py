from django.urls import path
from .views import *

urlpatterns = [
    path('', index_certs, name='home'),
    path('user/<int:user_id>/', get_user, name='user'),
]