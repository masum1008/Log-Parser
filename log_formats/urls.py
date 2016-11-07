from django.conf.urls import url
from .views import logformat_add_page, logformat_edit_page, logformat_list_page, logformat_delete_page


urlpatterns = [
    url(r'^add/$', logformat_add_page, name='logformat_add'),
    url(r'^(?P<id>\d+)/edit/$', logformat_edit_page, name='logformat_edit'),
    url(r'^list/$', logformat_list_page, name='logformat_list'),
    url(r'^(?P<id>\d+)/delete/$', logformat_delete_page, name='logformat_delete'),
]
