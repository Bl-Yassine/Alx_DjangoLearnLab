from django.contrib import admin
from .models import Book
# Register your models here.
admin.site.register(Book)

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','publication_year')
    search_fields=('title','author','publication_year')
    list_filter=('title','author','publication_year')

admin.site.register(Book , BookAdmin)

from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
admin.site.register(CustomUser, CustomUserAdmin)