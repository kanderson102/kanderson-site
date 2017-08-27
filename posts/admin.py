from django.contrib import admin
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title','content']

admin.site.register(Post, PostModelAdmin)
