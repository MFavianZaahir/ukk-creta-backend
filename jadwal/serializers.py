from rest_framework import serializers
from jadwal.models import Jadwal
from kereta.models import Kereta

class JadwalSerializer(serializers.ModelSerializer):
    kelas = serializers.CharField(source='kereta.kelas')
    nama_kereta = serializers.CharField(source='kereta.nama_kereta')

    class Meta:
        model = Jadwal
        fields = [
            'id', 
            'nama_kereta',
            'kelas',
            'asal_keberangkatan',
            'tujuan_keberangkatan',
            'tanggal_berangkat',
            'tanggal_kedatangan',
            'harga'
        ]