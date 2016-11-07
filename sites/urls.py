from django.conf.urls import url
from .views import site_add_page, site_edit_page, site_list_page, site_delete_page


urlpatterns = [
    url(r'^add/$', site_add_page, name='site_add'),
    url(r'^(?P<id>\d+)/edit/$', site_edit_page, name='site_edit'),
    url(r'^list/$', site_list_page, name='site_list'),
    url(r'^(?P<id>\d+)/delete/$', site_delete_page, name='site_delete'),
]
