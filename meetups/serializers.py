from rest_framework import serializers
from .models import meetup

class meetupSerializer(serializers.ModelSerializer):
    class Meta:
        model = meetup
        fields = '__all__'