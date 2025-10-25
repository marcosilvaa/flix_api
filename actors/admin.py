from django.contrib import admin
from actors.models import Actors

@admin.register(Actors)
class ActorsAdmin(admin.ModelAdmin):
    list_display = ('id','name')