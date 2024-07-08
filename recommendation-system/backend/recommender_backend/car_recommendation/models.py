from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    year = models.IntegerField()
    mpg = models.CharField(max_length=50)
    transmission = models.CharField(max_length=50)
    doors = models.IntegerField()
    submodel = models.CharField(max_length=255)
    msrp = models.FloatField()
    rating = models.CharField(max_length=1)
    consumer_rating = models.FloatField()
    photo = models.URLField()

    def __str__(self):
        return f'{self.make} {self.model} ({self.year})'
