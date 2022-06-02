from django.urls import path
from .views import *

urlpatterns = [
    path('', index_certs),
    path('csp/', csp),
    path('ctp/', ctp),
]