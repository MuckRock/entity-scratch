from .models import Entity
from rest_framework import serializers
from django.contrib.auth.models import User, Group


class EntitySerializer(serializers.HyperlinkedModelSerializer):
    # entities = serializers.PrimaryKeyRelatedField(
    #     many=True, queryset=Entity.objects.all()
    # )
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Entity
        fields = [
            "id",
            "wikidata_id",
            "name",
            "owner",
            "description",
            "created_at",
            "updated_at",
            "access",
        ]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "entities"]


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ["url", "name"]
