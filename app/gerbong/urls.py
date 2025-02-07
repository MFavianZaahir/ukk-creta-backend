from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GerbongViewSet

router = DefaultRouter()
router.register(r'', GerbongViewSet)

urlpatterns = [
    path('', include(router.urls)),
]