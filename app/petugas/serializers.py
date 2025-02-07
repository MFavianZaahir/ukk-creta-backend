from rest_framework import serializers
from .models import Petugas

class PetugasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Petugas
        fields = ['id', 'nama_petugas', 'alamat', 'telp', 'user']
        read_only_fields = ['user']
