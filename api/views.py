import django_filters
from rest_framework import viewsets, filters

from web.models import Node
from web.models import User
from .serializer import NodeSerializer
from .serializer import UserSerializer

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
