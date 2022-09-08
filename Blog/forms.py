from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder':'my title'}))
    
