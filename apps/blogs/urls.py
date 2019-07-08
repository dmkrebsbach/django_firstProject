from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index),
    url('^new$', views.new),
    url('^create$', views.index),
    url(r'^(?P<number>\d+)$', views.show),
    url(r'^(?P<number>\d+)/edit$', views.edit),
    url(r'^(?P<number>\d+)/delete$', views.destroy),   
]