from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.list, name='list'),
    url(r'^(?P<slug>[-\w]+)/$', views.watch, name='watch'),
]
