from .models import meetup
from rest_framework import viewsets, permissions
from .serializers import meetupSerializer

# meetup Viewset
class meetupViewSet(viewsets.ModelViewSet):
    queryset = meetup.objects.all()
    permissions_classes = [
        permissions.AllowAny
    ]

    serializer_class = meetupSerializer