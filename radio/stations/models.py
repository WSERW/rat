from django.db import models
from django.urls import reverse

# Create your models here.


class Station(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)
    image = models.ImageField(upload_to='stations', blank=True)
    frequency = models.FloatField()

    class Meta:
        ordering = ('name',)
        verbose_name = 'радиостанции'
        verbose_name_plural = 'радиостанции'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('stations:station_detail',
                    args=[self.slug])

class Singer(models.Model):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Испольнитель'
        verbose_name_plural = 'Исполнитель'

class Track(models.Model):
    name = models.CharField(max_length=40, db_index=True)
    album = models.CharField(max_length=40, default='-')
    singer = models.ForeignKey(Singer, related_name='traks', on_delete=models.CASCADE)
    ganre = models.CharField(max_length=30, default='-')
    duration = models.DurationField(null=True)
    station = models.ForeignKey(Station, related_name='traks', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='{}/traks'.format(station), blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name = 'Трек'
        verbose_name_plural = 'Трек'