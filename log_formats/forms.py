from django import forms
from django.forms import Textarea
from .models import LogFormats


class LogFormatForm(forms.ModelForm):
    class Meta:
        model = LogFormats
        fields = [
            "site",
            "log_format",
        ]
        widgets = {
            'log_format': Textarea(attrs={'cols': 50, 'rows': 10, 'placeholder': 'e.g. %h %l %u %t \\"%r\\\" %>s %b \\\"%{Referer}i\\\" \\\"%{User-Agent}i\\\"'}),

        }
