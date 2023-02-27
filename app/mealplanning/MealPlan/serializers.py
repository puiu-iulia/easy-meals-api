from rest_framework import serializers

from ..models import MealPlan, Meal
from ..serializers import MealDetailsSerializer, MealSerializer
from recipes.serializers import RecipeSerializer, RecipeIdSerializer
from recipes.models import Recipe


class MealPlanSerializer(serializers.ModelSerializer):
    """Serializer for daily meal plan"""

    recipes = RecipeIdSerializer(many=True)

    class Meta:
        model = MealPlan
        fields = ('id', 'date', 'recipes')

    def create(self, validated_data):
        meals = validated_data.pop('meals', [])
        recipes = validated_data.pop('recipes', [])
        meal_plan = MealPlan.objects.create(**validated_data)
        self._get_or_create_recipes(recipes, meal_plan)

        return meal_plan

    def _get_or_create_recipes(self, recipes, meal_plan):
        auth_user = self.context['request'].user
        for recipe in recipes:
            recipe_obj, created = Recipe.objects.get_or_create(
                user=auth_user,
                **recipe,
            )
            meal_plan.recipes.add(recipe_obj)


class MealPlanDetailsSerializer(serializers.ModelSerializer):

    recipes = RecipeSerializer(many=True)

    class Meta:
        model = MealPlan
        fields = ('id', 'date', 'recipes')
        read_only_fields = ('id',)

    def _get_or_create_meals(self, meals, meal_plan):
        auth_user = self.context['request'].user
        for meal in meals:
            meal_obj, created = Meal.objects.get_or_create(
                user=auth_user,
                **meal,
            )
            meal_plan.meals.add(meal_obj)
