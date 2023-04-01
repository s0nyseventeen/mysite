from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    print(f'{request=}')
    print(type(request))
    print('__dict__', request.__dict__)
    print('dir', dir(request))
    return HttpResponse('hello world from polls app')
