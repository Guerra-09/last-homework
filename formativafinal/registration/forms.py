from .models import UserProfile
from django import forms

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'last_name']
        widgets = {
            'name':forms.TextInput({'class':'form-control'}),
            'last_name':forms.TextInput({'class':'form-control'})
        }