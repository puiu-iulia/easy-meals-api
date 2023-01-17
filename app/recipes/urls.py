from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TagViewSet, IngredientViewSet, StepViewSet, RecipeViewSet


router = DefaultRouter()
router.register('tags', TagViewSet)
router.register('ingredients', IngredientViewSet)
router.register('steps', StepViewSet)
router.register('recipes', RecipeViewSet)

app_name = 'recipes'

urlpatterns = [
    path('', include(router.urls))
]
