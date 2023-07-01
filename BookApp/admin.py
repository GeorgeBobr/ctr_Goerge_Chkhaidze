from django.contrib import admin

from BookApp.models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'author', 'email', 'text', 'status', 'created_at', 'updated_at']
    list_display_links = ['id', 'author', 'status']
    list_filter = ['status']
    search_fields = ['author', 'text']
    fields = ['author', 'email', 'text', 'status', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


admin.site.register(Book, BookAdmin)