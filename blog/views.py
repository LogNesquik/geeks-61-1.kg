from django.shortcuts import render
from django.http import HttpResponse


def hello_world_view(request):
    if request.method == 'GET':
        return HttpResponse('Hello World!')
    

def name(request):
    if request.method == 'GET':
        return HttpResponse('<strong>Miroslav</strong>')
    

def photo(request):
    if request.method == 'GET':
        return HttpResponse('<img src="https://m.media-amazon.com/images/I/71s3cEqEZTL._AC_UF894,1000_QL80_.jpg">')