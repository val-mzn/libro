from django.http import HttpResponse

def list(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def bookitem_list(request, id_catalog):
    return HttpResponse("Hello, world. You're at the polls index.")

def bookitem_detail(request, id_catalog, id_books):
    return HttpResponse("Hello, world. You're at the polls index.")

def bookitem_create(request, id_catalog):
    return HttpResponse("Hello, world. You're at the polls index.")

def bookitem_delete(request, id_catalog, id_books):
    return HttpResponse("Hello, world. You're at the polls index.")

def bookitem_update(request, id_catalog, id_books):
    return HttpResponse("Hello, world. You're at the polls index.")