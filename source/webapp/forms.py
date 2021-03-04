from django import forms
from webapp.models import STATUS_CHOICES


class ArticleForm(forms.Form):
    title = forms.CharField(max_length=120, required=True)
    detail_description = forms.CharField(max_length=3000, required=True, widget=forms.Textarea)
    status = forms.ChoiceField(required=True, choices=STATUS_CHOICES, initial='new')
    date = forms.DateField(required=False)