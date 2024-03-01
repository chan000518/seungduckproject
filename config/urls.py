from django.contrib import admin
from django.urls import path, include
from apps.recommends import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.recommends.urls')),
    path('', include('users.urls') ),
    path('foods/', include('apps.foods.urls') ),
    path('lucks/', include('apps.lucks.urls') ),
    path('weather/', include('apps.weather.urls') ),
    path('soccers/', include('apps.soccers.urls') ),
]
