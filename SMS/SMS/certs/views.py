from django.shortcuts import render
from django.http import HttpResponse

from .models import Certs


def index_certs(request):
    certs = Certs.objects.all()
    context = {
        'certs': certs,
        'exam_name': 'Все сертификаты'
    }
    return render(request, 'certs/index_certs.html', context)


def csp(request):
    return HttpResponse('CSP certificates')


def ctp(request):
    return HttpResponse('CTP certificates')
