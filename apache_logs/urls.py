from django.conf.urls import include, url
from .views import create,parseLog,loadLogFormat,log_list



urlpatterns = [
    url(r'^uploadlog/$', create, name='uploadlog'),
    url(r'^parse/$', parseLog, name='parse'),
    url(r'^loadlogformat/$', loadLogFormat, name='loadLogFormat'),
    url(r'^loglist/$', log_list, name='loglist'),
    url(r'^table/', include('table.urls'))
]
