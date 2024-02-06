from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class useradmin(UserAdmin):
    list_display = ('username', 'email', 'name', 'score', 'is_staff',)
    
admin.site.register(User, useradmin)
