from actors.models import Actor
from rest_framework import serializers


class ActorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Actor
        fields = '__all__'