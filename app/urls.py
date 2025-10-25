from django.contrib import admin
from django.urls import path
from django.http import JsonResponse

def hello_view(request):
    return JsonResponse({'message':'Hellow World'})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_view)
]
