from django.db import models

class Coords(models.Model):
    id = models.IntegerField(primary_key=True)
    latitude = models.DecimalField(decimal_places=4, max_digits=9)
    longitude = models.DecimalField(decimal_places=4, max_digits=9)

    def __str__(self):
        return self.id
