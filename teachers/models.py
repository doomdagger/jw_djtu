from django.db import models


# Create your models here.
class Teacher(models.Model):
    full_name = models.CharField()

    def __str__(self):
        return self.full_name

