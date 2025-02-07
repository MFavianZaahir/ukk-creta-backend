from rest_framework import viewsets, permissions
from .models import Petugas
from .serializers import PetugasSerializer

class IsPetugas(permissions.BasePermission):
    """
    Custom permission to allow only Petugas to access.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'petugas'

class PetugasViewSet(viewsets.ModelViewSet):
    queryset = Petugas.objects.all()
    serializer_class = PetugasSerializer
    permission_classes = [IsPetugas]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
