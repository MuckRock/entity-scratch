from entity_project.entity_app.permissions import IsOwnerOrReadOnly
from .models import Entity
from rest_framework import viewsets
from rest_framework import permissions
from entity_project.entity_app.serializers import (
    EntitySerializer,
    UserSerializer,
    GroupSerializer,
)
from django.contrib.auth.models import User, Group
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


class EntityViewSet(viewsets.ModelViewSet):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        permission_classes = self.permission_classes
        if self.action in ["update", "partial_update", "delete"]:
            permission_classes = [
                permissions.IsAuthenticatedOrReadOnly,
                IsOwnerOrReadOnly,
            ]
        return [permission() for permission in permission_classes]


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all().order_by("-date_joined")
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(["GET"])
def api_root(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
            "entities": reverse("entity-list", request=request, format=format),
        }
    )
