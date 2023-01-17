from django.conf import settings
from django.db import models

from recipes.models import Recipe

from ..models import MealTime


class Meal(models.Model):
    """Meal model"""
    recipes = models.ManyToManyField(Recipe)
    meal_time = models.ForeignKey(MealTime, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    # def __str__(self):
    #     return self.id
