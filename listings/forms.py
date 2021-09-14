from django import forms
from listings.models import Listing
from listings.choices import state_choices
GEEKS_CHOICES =(
    ("1", "One"),
    ("2", "Two"),
    ("3", "Three"),
    ("4", "Four"),
    ("5", "Five"),
)


class ListForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'
        Listing.state = forms.MultipleChoiceField(
            required=False,
            widget=forms.CheckboxSelectMultiple,
            choices=state_choices,
        )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Name', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'city': forms.TextInput(attrs={'placeholder': 'City', 'class': 'form-control'}),
            'state': forms.TextInput(attrs={'placeholder': 'Region (All)', 'class': 'form-control'}),
            'zipcode': forms.TextInput(attrs={'placeholder': 'zipcode', 'class': 'form-control'}),
            'bedrooms': forms.TextInput(attrs={'placeholder': 'bedrooms', 'class': 'form-control'}),
            'bathrooms': forms.TextInput(attrs={'placeholder': 'bathrooms', 'class': 'form-control'}),
            'garage': forms.TextInput(attrs={'placeholder': 'garage', 'class': 'form-control'}),
            'sqft': forms.TextInput(attrs={'placeholder': 'sqft', 'class': 'form-control'}),
            'lot_size': forms.TextInput(attrs={'placeholder': 'lot_size', 'class': 'form-control'}),
            'property': forms.TextInput(attrs={'placeholder': 'property', 'class': 'form-control'}),
            'price': forms.TextInput(attrs={'placeholder': 'price', 'class': 'form-control'}),
            'listed_for': forms.TextInput(attrs={'placeholder': 'listed_for', 'class': 'form-control'}),
            'price_term': forms.TextInput(attrs={'placeholder': 'price_term', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'placeholder': 'description', 'class': 'form-control'}),

        }


