from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(request, nome, idade):
    return HttpResponse('Hello {} de {} anos'.format(nome, idade))