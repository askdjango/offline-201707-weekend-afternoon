from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^sum/(?P<numbers>[0-9/]+)/$', views.mysum),
]

