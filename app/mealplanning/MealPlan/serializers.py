from rest_framework import serializers

from ..models import MealPlan, Meal
from ..serializers import MealDetailsSerializer, MealSerializer


class MealPlanSerializer(serializers.ModelSerializer):
    """Serializer for daily meal plan"""

    class Meta:
        model = MealPlan
        fields = ('id', 'date', 'meals')
        read_only_fields = ('id',)


class MealPlanDetailsSerializer(serializers.ModelSerializer):

    meals = MealDetailsSerializer(many=True)

    class Meta:
        model = MealPlan
        fields = ('id', 'date', 'meals')
        read_only_fields = ('id',)

    def _get_or_create_meals(self, meals, meal_plan):
        auth_user = self.context['request'].user
        for meal in meals:
            meal_obj, created = Meal.objects.get_or_create(
                user=auth_user,
                **meal,
            )
            meal_plan.meals.add(meal_obj)

    def create(self, validated_data):
        meals = validated_data.pop('meals', [])
        meal_plan = MealPlan.objects.create(**validated_data)
        self._get_or_create_meals(meals, meal_plan)

        return meal_plan
