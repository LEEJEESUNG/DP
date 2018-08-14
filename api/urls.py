from rest_framework import routers
from .views import NodeViewSet
from .views import UserViewSet

router = routers.DefaultRouter()
router.register(r'nodes', NodeViewSet)
router.register(r'users', UserViewSet)
