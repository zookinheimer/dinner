from django.db import models


# Create your models here.
class dinner_list(models.Model):
    name = models.CharField(max_length=200)
    ingredients = models.TextField(blank=True)
    
    def __str__(self):
        return self.name

class history(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name