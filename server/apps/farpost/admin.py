from django.contrib import admin
from .models import Advert


@admin.register(Advert)
class AdvertAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'views', 'position',)
    list_filter = ('author',)
