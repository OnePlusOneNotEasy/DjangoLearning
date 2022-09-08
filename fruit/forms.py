from django import forms
from .models import Fruit

class FruitForm(forms.ModelForm):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder":"my-title"}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={"class":"new-class-name two",
                                                               "id":"my-id-for-exercise",
                                                               "rows":15,
                                                               "cols":20,
                                                               "placeholder":"my-descriptioin",})
                                 )
    price = forms.DecimalField(initial=99.99)
    class Meta:
        model = Fruit
        fields = [
            'title',
            'description',
            'price'
        ]

    def clean_title(self, *args, **kwargs):
        title = self.cleaned_data.get('title')
        if not 'apple' in title:
            raise forms.ValidationError('This is invalid.')
        return title

class RawFruitForm(forms.Form):
    title = forms.CharField(label='Title', widget=forms.TextInput(attrs={"placeholder":"my-title"}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={"class":"new-class-name two",
                                                               "id":"my-id-for-exercise",
                                                               "rows":15,
                                                               "cols":20,
                                                               "placeholder":"my-descriptioin",})
                                 )
    price = forms.DecimalField(initial=99.99)
