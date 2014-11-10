from django.conf.urls import patterns, url
from star import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)