from rest_framework import serializers

from .models import Step


class StepSerializer(serializers.ModelSerializer):
    """Serializer for step object"""

    class Meta:
        model = Step
        fields = ('id', 'title', 'description')
        read_only_fields = ('id',)
