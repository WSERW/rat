from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.stations_list, name='stations'),
    url(r'^(?P<slug>[-\w]+)/$',
        views.station_detail,
        name='station_detail'),
]