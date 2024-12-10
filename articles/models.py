from django.db import models

# Create your models here.

class Articles(models.Model):
    name = models.CharField(max_length=1000)
    discription = models.CharField(max_length=1000)

    def __str__(self):
        return self.name

   