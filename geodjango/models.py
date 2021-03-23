from django.db import models
from django.contrib.gis.db import models
from django.contrib.gis.db.models import PointField
from django.db.models import Manager as GeoManager

# Create your models here.


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    # location = models.PointField(srid=4326)
    objects = GeoManager()

    def __unicode__(self):
        return self.first_name

class Report(models.Model):
    name = models.CharField(max_length=30)
    categories = models.CharField(max_length=30)
    location = models.PointField(srid=4326)
    objects = GeoManager()
    description = models.TextField()
    picture = models.ImageField()

    @property
    def popupContent(self):
      return '<img src="{}" /><p><{}</p>'.format(
          self.picture.url,
          self.description)




class Entry(models.Model):
    point = PointField();

    @property
    def lat_lng(self):
        return list(getattr(self.point,'coords',[])[::-1 ])