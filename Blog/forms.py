from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={'placeholder':'my title'}))
    content = forms.CharField(required=False,
                              widget = forms.Textarea(attrs={"rows":15,
                                                             "cols":20,
                                                             "placeholder":"my content",})
                             )
    active = forms.BooleanField()
    class Meta:
        model = Article
        fields = [
                 'title',
                 'content',
                 'active'
                ]
