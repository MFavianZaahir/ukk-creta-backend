from rest_framework import serializers
from .models import Kursi

class KursiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kursi
        fields = '__all__'
