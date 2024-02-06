from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User

class userCreate(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'name')
    
    def __init__(self, *args, **kwargs):
        super(userCreate, self).__init__(*args, **kwargs)
        self.fields['username'].label = '아이디'
        self.fields['name'].label = '유저명'

class userChange(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = get_user_model()
        fields = ('username', 'name')

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'name']
