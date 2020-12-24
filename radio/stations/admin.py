from django.contrib import admin
from .models import Station, Singer, Track
# Register your models here.

class StationAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'frequency']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Station, StationAdmin)

class TrackAdmin(admin.ModelAdmin):
    list_display = ['name', 'album', 'singer', 'ganre', 'duration', 'station']
    list_filter = ['name', 'album', 'singer','ganre','duration','station']
    list_editable = ['album', 'singer','ganre']
    # prepopulated_fields = {'slug': ('name',)}
admin.site.register(Track, TrackAdmin)

class SingerAdmin(admin.ModelAdmin):
    list_display = ['name',]
admin.site.register(Singer, SingerAdmin)
