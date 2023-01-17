from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import Meal
from ..serializers import MealSerializer, MealDetailsSerializer


class MealViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """Manage meal times in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Meal.objects.all()
    serializer_class = MealDetailsSerializer

    def get_queryset(self):
        '''Return objects for the authenticated user only'''
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return MealDetailsSerializer

        return self.serializer_class
