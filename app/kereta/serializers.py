from rest_framework import serializers
from .models import Kereta

class KeretaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kereta
        fields = '__all__'