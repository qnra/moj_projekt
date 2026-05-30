from django.db import models


class Pomiar(models.Model):
    distance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.distance} cm"