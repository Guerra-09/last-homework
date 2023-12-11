from .models import Resena
import django.forms as forms
from django.core.exceptions import ValidationError

class ResenaForm(forms.ModelForm):
    class Meta:
        model = Resena
        fields = ['nombre', 'description', 'valoracion', 'photo']

        widgets = {
            'nombre' : forms.TextInput(attrs={'class':'form-control'}),
            'description' : forms.TextInput(attrs={'class':'form-control'}),
            'valoracion' : forms.NumberInput(attrs={'class':'form-control'}),
            'photo' : forms.ClearableFileInput(attrs={'class':'form-control'}),
        }

    def clean_rating(self):
        valoracion = self.cleaned_data.get('valoracion')

        if valoracion is not None and valoracion > 5:
            raise ValidationError("El rating no puede ser mayor a 5.")

        return valoracion


        