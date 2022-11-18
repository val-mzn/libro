from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.CharField(max_length=500)
    birth_date = models.DateField()

class Book(models.Model):
    name = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    overview = models.CharField(max_length=500)
    publisher = models.CharField(max_length=50)
    publicationDate = models.DateField()
    authors = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    isbn = models.CharField(max_length=20)

class BookItem(models.Model):
    LANGUAGES = [
        ('FR', 'Français'),
        ('DE', 'German'),
        ('SP', 'Spanish'),
        ('IT', 'Italian'),
        ('EN', 'English'),
    ]
    FORMATS = [
        ('PB', 'Paperback'),
        ('HC', 'Hardcover'),
        ('ABK', 'Audiobook'),
        ('ACD', 'Audio CD'),
        ('MP3', 'MP3 CD'),
        ('PDF', 'PDF'),
    ]
    title = models.CharField(max_length=50)
    barcode = models.CharField(max_length=20)
    number_of_page = models.IntegerField()
    lang = models.CharField(max_length=2, choices=LANGUAGES, default='Français')
    format = models.CharField(max_length=3, choices=FORMATS, default='Paperback')
    boworred = models.DateField()
    is_referece_only = models.BooleanField()

class FullName(models.Model):
    first = models.CharField(max_length=50)
    last = models.CharField(max_length=50)

class Account(models.Model):
    ACCOUNT_STATUS = [
        ('FROZEN', 'Frozen'),
        ('CLOSED', 'Closed'),
        ('ACTIVE', 'Active'),
    ]
    name = models.OneToOneField(
        FullName,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    opened = models.DateField()
    status = models.CharField(max_length=6, choices=ACCOUNT_STATUS, default='Active')

class Patron(models.Model):
    name = models.OneToOneField(
        FullName,
        on_delete=models.CASCADE,
        primary_key=True,
    )

class Catalogue(models.Model):
    books = models.ForeignKey(BookItem, on_delete=models.SET_NULL, null=True)

class Library(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    catalogue = models.OneToOneField(
        Catalogue,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    accounts = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
