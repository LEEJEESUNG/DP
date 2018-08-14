from rest_framework import serializers

from web.models import Node
from web.models import User

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ('data', 'visible')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('name', 'mail', 'password', 'salt')