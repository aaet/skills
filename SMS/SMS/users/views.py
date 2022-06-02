from django.shortcuts import render
from django.http import HttpResponse


def index_users(request):
    return HttpResponse('Hello users')


def technical_support(request):
    return HttpResponse('Technical support specialists')


def solution_managers(request):
    return HttpResponse('Solution managers')



