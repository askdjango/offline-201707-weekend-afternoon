from django import forms
from .models import Post

'''
class PostForm(forms.Form):
    author = forms.CharField()
    title = forms.CharField()
    content = forms.CharField()
'''

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        # fields = ['author', 'title', 'content']

