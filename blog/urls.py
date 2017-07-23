from django.conf.urls import url
from . import views
from . import views_cbv

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new/$', views_cbv.post_new, name='post_new'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^(?P<pk>\d+)/edit/$', views_cbv.post_edit, name='post_edit'),
    url(r'^(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
    url(r'^sum/(?P<numbers>[0-9/]+)/$', views.mysum, name='mysum'),
]

