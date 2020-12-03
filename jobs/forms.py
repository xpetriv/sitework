from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'city', 'full_text', 'published_date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Посада'
            }),
            "city": TextInput(attrs={
                'class': 'form-control',
                'placeholder':'Місто'
            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder':'Коротке резюме'
            }),
            "published_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder':'Дата публікації'
            })
        }    