import imaplib
from django import forms
from .models import Apply,Job

class ApplyForm(forms.ModelForm):
    class Meta:
        model=Apply
        fields=['name','email','portfolio_url','cv','cover_letter']


class AddForm(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        exclude=('slug','owner')