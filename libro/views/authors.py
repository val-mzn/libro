from django.http import HttpResponse
from django.shortcuts import render
from ..models import Author

def list(request):
    context = {"authors": Author.objects.all()}
    return render(request,"authors/author_list.html", context)

def detail(request, id):
    try:
        author = Author.objects.get(id=id)
        if author:
            context = {"author": author}
            return render(request,"authors/author_detail.html", context)
        else:
            return HttpResponse(status=404)
    except:
        return HttpResponse(status=500)

def create(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def delete(request, id):
    try:
        Author.objects.filter(id=id).delete()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=404)

def update(request, id):
    try:
        author = Author.objects.get(id=id)
        if author:
            context = {"author": author}
            return render(request,"authors/author_detail.html", context)
        else:
            return HttpResponse(status=404)
    except:
        return HttpResponse(status=500)