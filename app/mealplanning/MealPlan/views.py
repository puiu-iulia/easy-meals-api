from datetime import datetime
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import MealPlan
from ..serializers import MealPlanSerializer, MealPlanDetailsSerializer


class MealPlanViewSet(viewsets.ModelViewSet):
    """Manage meal times in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer

    def _params_to_ints(self, qs):
        """Convert a list of strings to integers."""
        return [int(str_id) for str_id in qs.split(',')]

    def get_queryset(self):
        '''Return objects for the authenticated user only'''
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new recipe."""
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return MealPlanDetailsSerializer

        return self.serializer_class
