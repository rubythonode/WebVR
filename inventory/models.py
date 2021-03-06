from __future__ import unicode_literals

from django.db import models

class House(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200, default="https://raw.githubusercontent.com/aframevr/aframe/master/examples/boilerplate/panorama/puydesancy.jpg")
    description = models.CharField(max_length=200, default="Good Room")

class Room(models.Model):
    description = models.CharField(max_length=200)
    url = models.URLField(max_length=200, default="https://raw.githubusercontent.com/aframevr/aframe/master/examples/boilerplate/panorama/puydesancy.jpg")
    house_id = models.CharField(max_length=200)
    def allarr(self):
        arrow = ConnectedArrow.objects.get(room_id=self.id)
        return arrow

class ConnectedArrow(models.Model):
    room_id = models.CharField(max_length=200)
    room_destination_id = models.CharField(max_length=100, default=1)
    arrow_degree = models.CharField(max_length=200)
    position = models.CharField(max_length=100, default='0 0 0')
    rotation = models.CharField(max_length=100, default='0 0 0')