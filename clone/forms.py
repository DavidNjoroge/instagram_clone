from django import forms
from django.contrib.auth.models import User
from . models import Profile,Post


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('bio', 'phone_number', 'gender')

class ProfilePicForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=('profile_pic',)

class NewPostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=('post_image',)
        
    # image=forms.ImageField()