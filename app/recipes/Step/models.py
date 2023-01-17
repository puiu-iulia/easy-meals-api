from django.conf import settings
from django.db import models


class Step(models.Model):
    """Step for recipes"""
    title = models.CharField(max_length=90)
    description = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
