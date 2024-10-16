from django import forms
from .models import Monument

class MonumentForm(forms.ModelForm):
    class Meta:
        model = Monument
        fields = ['name', 'from_person', 'monument', 'category', 'weight', 'length', 'width', 'height', 'quantity', 'status']
        widgets = {
            'status': forms.Select(choices=[
                ('owner', 'Owner'),
                ('polisher', 'Polisher'),
                ('designer', 'Designer'),
                ('stock', 'Stock'),
            ])
        }
