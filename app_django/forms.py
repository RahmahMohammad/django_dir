from django import forms
from .models import Blogers, Blogs

class BlogerForm(forms.ModelForm):

    class Meta:
        model = Blogers
        fields = ('name', 'nationality', 'photo_url',)


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blogs
        fields = ('title', 'bloger',)
