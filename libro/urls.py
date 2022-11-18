from django.contrib import admin
from django.urls import path
from .views import authors, books, catalogs

urlpatterns = [

    path('authors', authors.list, name='author_list'),
    path('author/detail/<id>', authors.detail, name='author_detail'),
    path('author/create', authors.create, name='author_create'),
    path('author/delete/<id>', authors.delete, name='author_delete'),
    path('author/update/<id>', authors.update, name='author_update'),

    path('books', books.list, name='book_list'),
    path('book/detail/<id>', books.detail, name='book_detail'),
    path('book/create', books.create, name='book_create'),
    path('book/delete/<id>', books.delete, name='book_delete'),
    path('book/update/<id>', books.update, name='book_update'),

    path('catalogs', catalogs.list, name='catalog_list'),
    path('catalog/<id_catalog>/bookitems', catalogs.bookitem_list, name='catalog_bookitem_list'),
    path('catalog/<id_catalog>/bookitem/detail/<id_book>', catalogs.bookitem_detail, name='catalog_bookitem_detail'),

    path('catalog/<id_catalog>/bookitem/create', catalogs.bookitem_create, name='catalog_bookitem_create'),
    path('catalog/<id_catalog>/bookitem/delete/<id_book>', catalogs.bookitem_delete, name='catalog_bookitem_delete'),
    path('catalog/<id_catalog>/bookitem/update/<id_book>', catalogs.bookitem_update, name='catalog_bookitem_update'),

    path('admin/', admin.site.urls),
]
