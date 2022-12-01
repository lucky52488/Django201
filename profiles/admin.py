from django.contrib import admin
from .models import Profile
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Post'''
    pass

admin.site.register(Profile, ProfileAdmin)