from .models import Vech
from django import forms

class vechForm(forms.ModelForm):
    class Meta:
        model=Vech
        fields = ['name', 'email', 'password']
        widgets ={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'}),


            
        }
