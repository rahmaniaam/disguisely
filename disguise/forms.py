from django import forms
from .models import Disguise, Document

class DisguiseForm(forms.ModelForm):
    class Meta:
        model = Disguise
        exclude = []

        widgets = {
        'dob': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
        }

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'