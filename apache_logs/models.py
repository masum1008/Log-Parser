from __future__ import unicode_literals

from django.db import models
from django.urls import reverse_lazy
from table import Table
from table.columns import Column,DatetimeColumn

from sites.models import Site
class ApacheLog(models.Model):
    # site = models.ForeignKey(Site, on_delete=models.CASCADE)
    local_ip = models.CharField(max_length=20, null=True)
    format_id =  models.IntegerField()
    site_id = models.IntegerField(null=True)
    status = models.IntegerField()
    response_bytes_clf = models.CharField(max_length=30,null=True)
    remote_host = models.CharField(max_length=50,null=True)
    request_method = models.CharField(max_length=4,null=True)
    request_url_path = models.CharField(max_length=500,null=True)
    time_received_tz = models.DateTimeField(max_length=50,null=True)
    time_received_tz_isoformat = models.CharField(max_length=50,null=True)
    time_us = models.CharField(max_length=50, null=True)
    unique_together = ('site_id','local_ip','status','time_received_tz_isoformat','request_url_path','response_bytes_clf','request_method')

class LogTable(Table):
    remote_host =Column(field='remote_host', header='IP')
    request_method = Column(field='request_method', header='Method')
    status = Column(field='status', header='Status Code')
    response_bytes_clf = Column(field='response_bytes_clf', header='Response Byte')
    time_received_tz = DatetimeColumn(field='time_received_tz', header='Time')
    request_url_path = Column(field='request_url_path', header='Request URL')

    class Meta:
        model = ApacheLog
        ajax = True
        template_name = 'buttons_table.html'

