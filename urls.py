from django.contrib import admin
from django.urls import path
from .views import BookPage, Books, AuthorPage, BookEdit

app_name = 'library'

urlpatterns = [
    path('', Books.as_view(), name="home"),
    path('books/', BookPage.as_view(), name="book_page"),
    path('authors/', AuthorPage.as_view(), name="author_page"),
    path('add/', BookEdit.as_view(), name="add_author")
]
