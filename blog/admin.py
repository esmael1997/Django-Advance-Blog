from django.contrib import admin
from .models import Category, Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status','category', 'created_date','published_date']
admin.site.register(Category)
admin.site.register(Post)