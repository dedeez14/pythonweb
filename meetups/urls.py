from rest_framework import routers
from .api import meetupViewSet

router = routers.DefaultRouter()
router.register('api/meetup', meetupViewSet, 'meetup')

urlpatterns = router.urls