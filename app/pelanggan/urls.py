from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PelangganViewSet

router = DefaultRouter()
router.register(r'', PelangganViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
