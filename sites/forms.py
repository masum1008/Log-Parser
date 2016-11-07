from django import forms
from .models import Site
from django.forms import TextInput


class SiteForm(forms.ModelForm):
    class Meta:
        model = Site

        fields = [
            "site_name",
            "site_url",
        ]
        widgets = {
            'site_url': TextInput(),
        }