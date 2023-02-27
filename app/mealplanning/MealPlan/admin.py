from django.contrib import admin
from .models import MealPlan


class MealPlanAdmin(admin.ModelAdmin):
    list_display = ('date', 'user')


admin.site.register(MealPlan, MealPlanAdmin)
