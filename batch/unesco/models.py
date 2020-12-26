from django.db import models

class Category(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        print(self.name)

class States(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        print(self.name)

class Region(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        print(self.name)

class Iso(models.Model):
    name = models.CharField(max_length = 128)

    def __str__(self):
        print(self.name)

class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    iso = models.ForeignKey(Iso, on_delete=models.CASCADE)

    description = models.TextField()
    justification = models.TextField()

    area_hectares = models.FloatField(null = True)
    longitude = models.FloatField(null = True)
    latitude = models.FloatField(null = True)


    def __str__(self):
        print(self.name)