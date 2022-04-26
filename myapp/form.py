from dataclasses import fields
from django import forms
from myapp.models import Vocab

class vocabForm(forms.ModelForm):
    class Meta:
        model=Vocab
        fields='__all__'

