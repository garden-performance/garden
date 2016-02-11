from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^func/(?P<device_id>[\d]+)$', views.func),
]
