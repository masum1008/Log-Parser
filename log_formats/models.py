from __future__ import unicode_literals

from django.db import models


class LogFormats(models.Model):
    site_name = models.CharField(max_length=100)
    log_format = models.CharField(max_length=100)

    def __unicode__(self):
        return self.site_name
