from django.shortcuts import render, get_object_or_404
from .models import Station, Singer, Track

# Create your views here.

def stations_list(request,station_slug=None):
    station = None
    stations = Station.objects.all()
    if station_slug:
        station = get_object_or_404(Station, slug=station_slug)
    return render(request, 'stations/index.html', {'station':station,
                                                    'stations':stations})

def station_detail(request, slug):
    station = get_object_or_404(Station, slug=slug)
    tracks = Track.objects.filter(station=station)
    tracks = Track.objects.all()
    return render(request, 'stations/detail.html', {'station':station,
                                                    'tracks': tracks})