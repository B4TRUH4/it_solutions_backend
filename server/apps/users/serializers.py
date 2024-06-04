from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор модели пользователя"""
    class Meta:
        model = User
        fields = (
            'id', 'email', 'first_name', 'last_name',
            'password',
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }
