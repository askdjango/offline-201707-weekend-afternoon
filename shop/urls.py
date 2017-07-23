from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.item_list, name='item_list'),
    url(r'^(?P<pk>\d+)/$', views.item_detail, name='item_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views.item_edit, name='item_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.item_delete, name='item_delete'),
    url(r'^new/$', views.item_new, name='item_new'),
]

