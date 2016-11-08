from django import forms
from .models import Site

class SiteForm(forms.ModelForm):
    class Meta:
        model = Site

        fields = [
            "site_name",
            "site_url",
        ]
