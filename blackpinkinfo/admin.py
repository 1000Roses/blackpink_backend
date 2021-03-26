from django.contrib import admin
from .models import Member, Song, Prize

array = [Member, Song, Prize]
admin.site.register(array)
