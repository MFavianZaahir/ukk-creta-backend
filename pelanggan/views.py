from rest_framework import viewsets, permissions
from pelanggan.models import Pelanggan
from pelanggan.serializers import PelangganSerializer

class IsPetugas(permissions.BasePermission):
    """
    Custom permission to allow only Petugas to access.
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'petugas'

class PelangganViewSet(viewsets.ModelViewSet):
    """
    CRUD API for Pelanggan (Only Petugas can manage)
    """
    queryset = Pelanggan.objects.all()
    serializer_class = PelangganSerializer
    permission_classes = [IsPetugas]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
