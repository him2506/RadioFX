from django.db import models

# Create your models here.
class Station(models.Model):
    station_id = models.AutoField(primary_key = True)
    station_name = models.CharField(max_length=50)
    Slogan = models.CharField(max_length=50,default="")
    desc = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='images', default="")
    url = models.CharField(max_length=1000,default="")
    category = models.CharField(max_length=100,default="")
    state = models.CharField(max_length=100,default="")
    Language = models.CharField(max_length=100,default="")
    top = models.BooleanField(default=False)
    Pop = models.BooleanField(default=False)
    Rock = models.BooleanField(default=False)
    Electronic = models.BooleanField(default=False)
    Hip_Hop = models.BooleanField(default=False)
    Classic = models.BooleanField(default=False)
    Dance = models.BooleanField(default=False)
    LoveSongs = models.BooleanField(default=False)
    OldSongs = models.BooleanField(default=False)
    UnpluggedSongs = models.BooleanField(default=False)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.station_name