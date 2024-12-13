from django.contrib.auth.forms import UserCreationForm , UserChangeForm
from django.contrib.auth.models import User
from django import forms

class RegisterUserForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email' , 'password1', 'password2' )


class EditUserForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email' , 'password')


from .models import Post
from django.utils.timezone import now 
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title' , 'content' ]
        widgets = {
            'title' : forms.TextInput(attrs={'class' : 'form-control'}),
            'content' : forms.Textarea(attrs={'class':'form-control'})
            }