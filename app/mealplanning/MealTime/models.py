from django.conf import settings
from django.db import models


class MealTime(models.Model):
    """Meal Time for meal"""
    name = models.CharField(max_length=20)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
