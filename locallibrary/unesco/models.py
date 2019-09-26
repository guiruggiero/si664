from django.db import models

# Create your models here.

class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class States(models.Model) :
    name = models.CharField(max_length=64)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=64)

    def __str__(self) :
        return self.name

class ISO(models.Model) :
    name = models.CharField(max_length=2)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=2048)
    justification = models.CharField(max_length=4096, null=True)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    states = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(ISO, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name