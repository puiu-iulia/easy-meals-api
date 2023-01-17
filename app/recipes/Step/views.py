from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Step

from .serializers import StepSerializer


class StepViewSet(viewsets.GenericViewSet,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin):
    """Manage tags in the database"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Step.objects.all()
    serializer_class = StepSerializer

    def get_queryset(self):
        '''Return objects for the authenticated user only'''
        return self.queryset.filter(user=self.request.user).order_by('title')

    def perform_create(self, serializer):
        """Create a new ingredient"""
        serializer.save(user=self.request.user)
