from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PetugasViewSet

router = DefaultRouter()
router.register(r'', PetugasViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
