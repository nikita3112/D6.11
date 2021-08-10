from django.forms.formsets import formset_factory
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, CreateView
from library.models import Book, Author
from library.forms import BookForm
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
class Books(ListView):
    model = Book
    context_object_name = 'books'
    template_name = "home_page.html"

class BookPage(ListView):
    template_name = 'books_page.html'
    model = Book
    context_object_name = 'books_list'

class AuthorPage(ListView):
    template_name = "authors_page.html"
    model = Author
    context_object_name = 'authors'

class BookEdit(CreateView):  
    model = Book  
    form_class = BookForm
    success_url = reverse_lazy('library:book_page')  
    template_name = 'add_page.html'