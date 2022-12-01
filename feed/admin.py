from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    '''Admin View for Post'''
    pass

admin.site.register(Post, PostAdmin)