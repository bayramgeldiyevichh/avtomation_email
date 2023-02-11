from django.contrib.auth.forms import UserCreationForm
from django.db.models import fields  
from django import forms  
from .models import * 


from django import forms
from .models import User
from  .models import*


class ControlVideoForm(forms.ModelForm):
    class Meta:
        model = ControlVideo
        fields = "__all__"



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']