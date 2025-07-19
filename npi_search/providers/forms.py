from django import forms
from .models import US_STATES

class ProviderSearchForm(forms.Form):
    first_name = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'First Name'
        })
    )
    
    last_name = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Last Name'
        })
    )
    
    city = forms.CharField(
        required=False,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'City'
        })
    )
    
    state = forms.ChoiceField(
        required=False,
        choices=[('', 'Select State')] + US_STATES,
        widget=forms.Select(attrs={
            'class': 'form-control searchable-select'
        })
    )
    
    postal_code = forms.CharField(
        required=False,
        max_length=20,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Postal Code'
        })
    )
    
    taxonomy = forms.CharField(
        required=False,
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Taxonomy/Specialty (e.g., Family Medicine, Cardiology)'
        })
    )
    
    def clean(self):
        cleaned_data = super().clean()
        # check if at least one field has data
        fields_to_check = ['first_name', 'last_name', 'city', 'state', 'postal_code', 'taxonomy']
        has_data = any(cleaned_data.get(field) for field in fields_to_check)
        
        if not has_data:
            raise forms.ValidationError("Please enter at least one search criteria.")
        
        return cleaned_data