from django.contrib import admin
from .models import Song, Liked
# Register your models here.
admin.site.register(Song)
admin.site.register(Liked)