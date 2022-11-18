from django.http import HttpResponse
from models import Author

def list(request):

    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, id):
    return HttpResponse("Hello, world. You're at the polls index.")

def create(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def delete(request, id):
    return HttpResponse("Hello, world. You're at the polls index.")

def update(request, id):
    return HttpResponse("Hello, world. You're at the polls index.")