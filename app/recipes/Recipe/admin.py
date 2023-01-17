from django.contrib import admin

from .models import Recipe


class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']


admin.site.register(Recipe, RecipeAdmin)
