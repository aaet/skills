from django.shortcuts import render
from django.http import HttpResponse

from .models import Certs, Users


def index_certs(request):
    certs = Certs.objects.all()
    context = {
        'certs': certs,
        'exam_name': 'Все сертификаты',
    }
    return render(request, 'certs/index_certs.html', context)


def get_user(request, user_id):
    certs = Certs.objects.filter(user_id=user_id)
    user = Users.objects.get(pk=user_id)
    return render(request, 'certs/users.html', {'certs': certs, 'user': user})
