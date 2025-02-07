from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import KursiViewSet

router = DefaultRouter()
router.register(r'', KursiViewSet)


urlpatterns = [
    path('', include(router.urls)),
]