from django import forms
from django.forms import Textarea, TextInput
from .models import Site


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site

        fields = [
            "site_name",
            "site_url",
        ]
        widgets = {
            'site_name': TextInput(attrs={'placeholder': 'Site Name'}),
            'site_url': TextInput(attrs={'placeholder': 'e.g. www.google.com'}),

        }