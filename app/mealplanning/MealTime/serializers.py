from rest_framework import serializers

from ..models import MealTime


class MealTimeSerializer(serializers.ModelSerializer):
    """Serializer for MealTime object"""

    class Meta:
        model = MealTime
        fields = ('id', 'name',)
        read_only_fields = ('id',)
