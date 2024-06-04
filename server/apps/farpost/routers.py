from rest_framework import routers

from .viewsets import AdvertViewSet

advert_router = routers.DefaultRouter()

advert_router.register(
    prefix="adverts",
    viewset=AdvertViewSet,
    basename="adverts",
)
