from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import MealTimeViewSet, MealViewSet, MealPlanViewSet

router = DefaultRouter()
router.register('/meal-times', MealTimeViewSet)
router.register('/meals', MealViewSet)
router.register('/mealplanning', MealPlanViewSet)

app_name = 'mealplanning'

urlpatterns = [
    path('', include(router.urls))
]
