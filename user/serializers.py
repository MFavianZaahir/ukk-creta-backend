from rest_framework import serializers
from django.contrib.auth import get_user_model
from petugas.models import Petugas
from pelanggan.models import Pelanggan

User = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']
        read_only_fields = ['username']

class PetugasProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petugas
        fields = ['nama_petugas', 'alamat', 'telp']

class PelangganProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = ['NIK', 'nama_penumpang', 'alamat', 'telp']
