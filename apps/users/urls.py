from django.urls import path
from .views import *

app_name = 'users'

urlpatterns = [
    path('', main, name='main'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('detail/', user_detail, name='user_detail'),
    path('delete/', user_delete, name='user_delete'),
    path('update/', user_update, name='user_update'),
    path('logout/', logout, name='logout'),
]
