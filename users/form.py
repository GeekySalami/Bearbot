from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    #image = forms.ImageField()
    class Meta():
        model = User
        fields = ['first_name','last_name','username', 'email', 'password1', 'password2']
    
    '''
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
    '''
'''
class UserUpdateForm(forms.ModelForm):
    model = User

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        field = ['image']
'''