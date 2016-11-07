__author__ = 'istiyak'

from django import forms

class SiteForm(forms.Form):
    name = forms.CharField(label="site_name", required=True)
    url = forms.CharField(label="site_url", required=True)