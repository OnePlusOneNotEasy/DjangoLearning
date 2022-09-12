from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = [
            'title'
        ]

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if title.lower() == 'abc':
            raise forms.ValidationError('title invalid')
        return title
