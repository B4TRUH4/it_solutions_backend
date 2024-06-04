from rest_framework import serializers
from .models import Advert


class AdvertSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра/создания объявления"""
    class Meta:
        model = Advert
        fields = '__all__'


class AdvertUpdateSerializer(serializers.ModelSerializer):
    """Сериализатор для обновления объявления"""
    class Meta:
        model = Advert
        # Исключен id, так как при его изменении возможно
        # создание дубликата объекта, но с измененным id
        # (происходит из-за возможности указания id)
        exclude = ('id',)
