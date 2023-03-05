from rest_framework import serializers

from ..models import MealPlan, Meal
from ..serializers import MealDetailsSerializer, MealSerializer
from recipes.serializers import RecipeSerializer, RecipeIdSerializer
from recipes.models import Recipe


class MealPlanSerializer(serializers.ModelSerializer):
    """Serializer for daily meal plan"""

    class Meta:
        model = MealPlan
        fields = ('id', 'date', 'recipes')

    def create(self, validated_data):
        recipes = validated_data.pop('recipes', [])
        meal_plan = MealPlan.objects.create(**validated_data)
        self._get_recipes(recipes, meal_plan)

        return meal_plan

    def _get_recipes(self, recipes, meal_plan):
        auth_user = self.context['request'].user
        for recipe in recipes:
            recipe_objs = Recipe.objects.filter(
                user=auth_user,
                id=recipe.id,  # Add additional fields as necessary
            )
        for recipe_obj in recipe_objs:
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
