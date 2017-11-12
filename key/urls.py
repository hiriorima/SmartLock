from rest_framework import routers
from .views import KeyViewSet

router = routers.DefaultRouter()
router.register(r'keys', KeyViewSet)
