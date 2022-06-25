from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book
from .forms import BookForm

'''
This book_pdf controls the the things we are going to view of the web page.
'''


# Create your views here.

def index(request):
    book_list = Book.objects.all()
    context = {
        'book_list': book_list
    }
    return render(request, 'myapp/index.html', context)


def details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, 'myapp/detail.html', {'book': book})


def add_book(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        description = request.POST.get('description', )
        price = request.POST.get('price', )
        author = request.POST.get('author', )
        book_pdf = request.FILES['book_pdf']
        book_image = request.FILES['book_image']
        genre = request.POST.get('genre', )
        book = Book(name=name, description=description, price=price, book_image=book_image, author=author, genre=genre,
                    book_pdf=book_pdf)
        book.save()
        return redirect('/')

    return render(request, 'myapp/add_book.html')


def update(request, id):
    book = Book.objects.get(id=id)

    form = BookForm(request.POST or None, request.FILES, instance=book)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'myapp/edit.html', {'form': form, 'book_pdf': book})


def delete(request, id):
    if request.method == "POST":
        book = Book.objects.get(id=id)
        book.delete()
        return redirect('/')
    return render(request, 'myapp/delete.html')


def search(request):
    search_book = request.GET.get('search')
    if search_book:
        book = Book.objects.filter(Q(name__icontains=search_book))
    else:
        book = Book.objects.all()
    return render(request, 'myapp/search_results.html', {'book': book})


def fantasy(request):
    book_item = Book.objects.all()
    book = []
    for i in book_item:
        if i.genre == 'Fantasy':
            book.append(i)
    context = {
        'book': book
    }
    return render(request, 'myapp/fantasy.html', context)


def comedy(request):
    book_item = Book.objects.all()
    book = []
    for i in book_item:
        if i.genre == 'comedy':
            book.append(i)
    context = {
        'book': book
    }
    return render(request, 'myapp/comedy.html', context)


def Finance(request):
    book_item = Book.objects.all()
    book = []
    for i in book_item:
        if i.genre == 'Finance':
            book.append(i)
    context = {
        'book': book
    }
    return render(request, 'myapp/Finance.html', context)


def Horror(request):
    book_item = Book.objects.all()
    book = []
    for i in book_item:
        if i.genre == 'Horror':
            book.append(i)
    context = {
        'book': book
    }
    return render(request, 'myapp/horror.html', context)
