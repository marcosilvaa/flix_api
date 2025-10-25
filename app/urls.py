from django.contrib import admin
from django.urls import path
from genres.views import GenreCreateListView, GenreRetrieveUpdateDestroyView
from actors.views import ActorsCreateListView, ActorsRetrieveUpdateDestroyView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('genres/', GenreCreateListView.as_view(), name='genre-create-list'),
    path('genres/<int:pk>/', GenreRetrieveUpdateDestroyView.as_view(), name='genre-detail-view'),
    path('actors/', ActorsCreateListView.as_view(), name='actors-create-list'),
    path('actors/<int:pk>/', ActorsRetrieveUpdateDestroyView.as_view(), name='actors-detail-view'),
]
