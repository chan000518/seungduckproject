from django.contrib import admin
from django.urls import path, include
from apps.recommends import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.recommends.urls')),
    path('', include('apps.users.urls') ),
    
]
