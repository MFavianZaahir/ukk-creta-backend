from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JadwalViewSet, JadwalListView

router = DefaultRouter()
router.register(r'', JadwalViewSet)
router.register(r'jadwal-list', JadwalListView, basename='jadwal-list')


urlpatterns = [
    path('', include(router.urls)),
]