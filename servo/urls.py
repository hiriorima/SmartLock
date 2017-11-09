from rest_framework import routers
from .views import ServoViewSet

router = routers.DefaultRouter()
router.register(r'servos', ServoViewSet)
