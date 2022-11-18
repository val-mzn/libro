from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from ..forms import AuthorForm
from ..models import Author

def list(request):
    context = {"authors": Author.objects.all()}
    return render(request,"authors/author_list.html", context)

def detail(request, id):
    author = Author.objects.get(id=id)
    if author:
        context = {"author": author}
        return render(request,"authors/author_detail.html", context)
    else:
        return HttpResponse(status=404)

def create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('author_list'))
    else:
        form = AuthorForm()
    return render(request, 'authors/author_create.html', {'form': form})

def delete(request, id):
    try:
        Author.objects.filter(id=id).delete()
        return HttpResponse(status=200)
    except:
        return HttpResponse(status=404)

def update(request, id):
    author = Author.objects.get(id=id)
    if author:
        context = {"author": author}
        return render(request,"authors/author_detail.html", context)
    else:
        return HttpResponse(status=404)
