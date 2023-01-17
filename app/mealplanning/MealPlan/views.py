from datetime import datetime
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from ..models import MealPlan
from ..serializers import MealPlanSerializer, MealPlanDetailsSerializer


class MealPlanViewSet(viewsets.GenericViewSet,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    """Manage meal times in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = MealPlan.objects.all()
    serializer_class = MealPlanSerializer
    current_date = datetime.today().date()

    def get_queryset(self):
        '''Return objects for the authenticated user only'''
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == 'list':
            return MealPlanDetailsSerializer

        return self.serializer_class
