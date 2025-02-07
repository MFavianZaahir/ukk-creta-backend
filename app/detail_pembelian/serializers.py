from rest_framework import serializers
from .models import DetailPembelian

class DetailPembelianSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetailPembelian
        fields = '__all__'