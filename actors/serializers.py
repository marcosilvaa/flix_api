from actors.models import Actors
from rest_framework import serializers


class ActorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actors
        fields = '__all__'