from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import MealTime
from ..serializers import MealTimeSerializer


class MealTimeViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    """Manage meal times in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = MealTime.objects.all()
    serializer_class = MealTimeSerializer

    def get_queryset(self):
        '''Return objects for the authenticated user only'''
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)
