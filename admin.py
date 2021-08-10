from django.contrib import admin
from library.models import Book, Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    @staticmethod
    def author_full_name(obj):
        return obj.author.full_name

    list_display = ('title', 'author_full_name',)
    fields = ('ISBN', 'title', 'image', 'description', 'year_release', 'author', 'price')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

