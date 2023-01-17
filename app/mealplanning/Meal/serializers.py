from rest_framework import serializers

from ..models import Meal
from ..serializers import MealTimeSerializer
from recipes.serializers import RecipeSerializer


class MealSerializer(serializers.ModelSerializer):
    """Serializer for meal object"""

    # recipes = RecipeSerializer(many=True)
    # meal_time = MealTimeSerializer(many=False)

    class Meta:
        model = Meal
        fields = ('id')
        read_only_fields = ('id',)


class MealDetailsSerializer(serializers.ModelSerializer):
    """Serializer for meal object"""

    recipes = RecipeSerializer(many=True)
    meal_time = MealTimeSerializer(many=False)

    class Meta:
        model = Meal
        fields = ('id', 'recipes', 'meal_time')
        read_only_fields = ('id',)
