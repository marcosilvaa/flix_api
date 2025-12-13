from django.db.models import Count
from rest_framework import generics, views, response, status
from rest_framework.permissions import IsAuthenticated
from movies.models import Movie
from movies.serializers import MovieModelSerializer
from app.permissions import GlobalDefaultPermission


class MovieCreateListView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    

class MovieRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    serializer_class = MovieModelSerializer
    
    
class MovieStatsView(views.APIView):
    permission_classes = (IsAuthenticated, GlobalDefaultPermission,)
    queryset = Movie.objects.all()
    
    
    def get(self, request):
        
        total_movies = self.queryset.count()
        movies_by_genre = self.queryset.values('genre__name').annotate(count=Count('id'))
        
        return response.Response(
            data = {'message', 'funcionou'},
            status = status.HTTP_200_OK
        )