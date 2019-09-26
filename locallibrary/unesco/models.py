from django.db import models

# Create your models here.

class Name(models.Model) :
    name = models.CharField(max_length=150)

    def __str__(self) :
        return self.name

class Description(models.Model) :
    text = models.CharField(max_length=1800)

    def __str__(self) :
        return self.text

class Justification(models.Model) :
    text = models.CharField(max_length=3700, null=True)

    def __str__(self) :
        return self.text

class Year(models.Model) :
    number = models.IntegerField()

    def __str__(self) :
        return self.number

class Longitude(models.Model) :
    number = models.FloatField()

    def __str__(self) :
        return self.number

class Latitude(models.Model) :
    number = models.FloatField()

    def __str__(self) :
        return self.number

class AreaHectares(models.Model) :
    name = models.FloatField(null=True)

    def __str__(self) :
        return self.name

class Category(models.Model) :
    name = models.CharField(max_length=10)

    def __str__(self) :
        return self.name

class State(models.Model) :
    name = models.CharField(max_length=60)

    def __str__(self) :
        return self.name

class Region(models.Model) :
    name = models.CharField(max_length=40)

    def __str__(self) :
        return self.name

class ISO(models.Model) :
    code = models.CharField(max_length=2)

    def __str__(self) :
        return self.code

class Site(models.Model):
    name = models.CharField(max_length=150)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    # ...

    def __str__(self) :
        return self.name