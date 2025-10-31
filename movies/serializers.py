from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


    
class MovieModelSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = '__all__'
        
    rate = serializers.SerializerMethodField(read_only=True)
    def get_rate(self, obj):    # obj = 
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate,1)        
        return None
        
        
        
    def validate_release_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError('A data de lançamento não pode ser anterior à 1990.')
        return value 
    
    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError('O resumo nao pode ser maior do que 200 carcteres.')
        return value
        