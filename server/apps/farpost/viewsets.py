from rest_framework import viewsets, permissions

from .models import Advert
from .serializers import AdvertSerializer, AdvertUpdateSerializer


class AdvertViewSet(viewsets.ModelViewSet):
    queryset = Advert.objects.all()
    serializer_class = AdvertSerializer
    serializer_dict = {
        'update': AdvertUpdateSerializer
    }

    def get_serializer_class(self):
        return self.serializer_dict.get(self.action, AdvertSerializer)
