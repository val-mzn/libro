from django.http import HttpResponse
from django.shortcuts import render
from models import Author

def list(request):
    context = {"authors": Author.objects.all()}
    return render(request,"libro/author_list.html", context)

def detail(request, id):
    return HttpResponse("Hello, world. You're at the polls index.")

def create(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def delete(request, id):
    return HttpResponse("Hello, world. You're at the polls index.")

def update(request, id):
    return HttpResponse("Hello, world. You're at the polls index.")