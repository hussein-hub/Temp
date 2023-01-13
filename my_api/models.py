from django.db import models


class Property(models.Model):
    name = models.CharField(max_length = 200)
    address = models.CharField(max_length = 1000)
    city = models.CharField(max_length = 50)
    state = models.CharField(max_length = 50)

    def __str__(self):
        return self.name
