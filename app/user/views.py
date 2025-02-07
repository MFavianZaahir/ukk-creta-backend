from rest_framework import generics, permissions
from user.serializers import UserProfileSerializer, PetugasProfileSerializer, PelangganProfileSerializer
from petugas.models import Petugas
from pelanggan.models import Pelanggan
from django.contrib.auth import get_user_model

User = get_user_model()

class ProfileUpdateView(generics.RetrieveUpdateAPIView):
    """
    Profile update API for both Petugas & Pelanggan
    """
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)

    def get_serializer_class(self):
        if self.request.user.role == 'petugas':
            return PetugasProfileSerializer
        elif self.request.user.role == 'pelanggan':
            return PelangganProfileSerializer
        return UserProfileSerializer

    def get_object(self):
        if self.request.user.role == 'petugas':
            return Petugas.objects.get(user=self.request.user)
        elif self.request.user.role == 'pelanggan':
            return Pelanggan.objects.get(user=self.request.user)
        return self.request.user
