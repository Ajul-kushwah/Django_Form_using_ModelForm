from django import forms
from .models import Student

class StudentRegister(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['firstname','lastname','email']
        widgets = {
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }
