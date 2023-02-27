from django.contrib import admin
from .models import Step


class StepAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'description')


admin.site.register(Step, StepAdmin)
