from rest_framework import serializers

from ..models import Recipe, Tag, Step, Ingredient
from ..serializers import TagSerializer, IngredientSerializer, StepSerializer


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""
    tags = TagSerializer(many=True, required=False)
    ingredients = IngredientSerializer(many=True, required=False)
    steps = StepSerializer(many=True, required=False)

    class Meta:
        model = Recipe
        fields = [
            'id', 'title', 'time_minutes', 'link', 'tags', 'description',
            'ingredients', 'steps', "image"
        ]
        read_only_fields = ['id']


class RecipeIdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = ('id',)


class RecipeDetailSerializer(RecipeSerializer):
    """Serializer for recipe detail view."""

    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields

    def _get_or_create_tags(self, tags, recipe):
        """Handle getting or creating tags as needed."""
        auth_user = self.context['request'].user
        for tag in tags:
            tag_obj, created = Tag.objects.get_or_create(
                user=auth_user,
                **tag,
            )
            recipe.tags.add(tag_obj)

    def _get_or_create_ingredients(self, ingredients, recipe):
        """Handle getting or creating ingredients as needed."""
        auth_user = self.context['request'].user
        for ingredient in ingredients:
            ingredient_obj, created = Ingredient.objects.get_or_create(
                user=auth_user,
                **ingredient,
            )
            recipe.ingredients.add(ingredient_obj)

    def _get_or_create_steps(self, steps, recipe):
        """Handle getting or creating steps as needed."""
        auth_user = self.context['request'].user
        for step in steps:
            step_obj, created = Step.objects.get_or_create(
                user=auth_user,
                **step,
            )
            recipe.step.add(step_obj)

    def create(self, validated_data):
        """Create a recipe."""
        tags = validated_data.pop('tags', [])
        ingredients = validated_data.pop('ingredients', [])
        steps = validated_data.pop('steps', [])
        recipe = Recipe.objects.create(**validated_data)
        self._get_or_create_tags(tags, recipe)
        self._get_or_create_ingredients(ingredients, recipe)
        self._get_or_create_steps(steps, recipe)

        return recipe

    def update(self, instance, validated_data):
        """Update recipe."""
        tags = validated_data.pop('tags', None)
        ingredients = validated_data.pop('ingredients', None)
        steps = validated_data.pop('steps', None)
        if tags is not None:
            instance.tags.clear()
            self._get_or_create_tags(tags, instance)
        if ingredients is not None:
            instance.ingredients.clear()
            self._get_or_create_ingredients(ingredients, instance)
        if steps is not None:
            instance.steps.clear()
            self._get_or_create_steps(steps, instance)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class RecipeImageSerializer(serializers.ModelSerializer):
    """Serializer for uploading images to recipes."""

    class Meta:
        model = Recipe
        fields = ['id', 'image']
        read_only_fields = ['id']
        extra_kwargs = {'image': {'required': 'True'}}
