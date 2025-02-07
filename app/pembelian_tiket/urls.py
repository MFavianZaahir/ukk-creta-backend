from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PembelianTiketViewSet

router = DefaultRouter()
router.register(r'', PembelianTiketViewSet)


urlpatterns = [
    path('', include(router.urls)),
]