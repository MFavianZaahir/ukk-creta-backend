from rest_framework import serializers
from .models import PembelianTiket

class PembelianTiketSerializer(serializers.ModelSerializer):
    class Meta:
        model = PembelianTiket
        fields = '__all__'
