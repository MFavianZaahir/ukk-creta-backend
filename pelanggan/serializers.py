from rest_framework import serializers
from pelanggan.models import Pelanggan

class PelangganSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pelanggan
        fields = ['id', 'NIK', 'nama_penumpang', 'alamat', 'telp', 'user']
        read_only_fields = ['user']
