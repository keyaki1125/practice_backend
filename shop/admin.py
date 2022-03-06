from django.contrib import admin

from .models import Book, Author


class BookModelAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'id', 'created_at',)
    ordering = ('created_at',)
    readonly_fields = ('id', 'created_at',)


class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'created_at',)
    ordering = ('created_at',)
    readonly_fields = ('id', 'created_at',)


admin.site.register(Book, BookModelAdmin)
admin.site.register(Author, AuthorModelAdmin)