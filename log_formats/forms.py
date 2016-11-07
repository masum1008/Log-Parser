from django import forms
from django.forms import Textarea
from .models import LogFormats


class LogFormatForm(forms.ModelForm):
    class Meta:
        model = LogFormats
        fields = [
            "site_name",
            "log_format",
        ]
        widgets = {
            'log_format': Textarea(attrs={'cols': 30, 'rows': 10}),

        }
