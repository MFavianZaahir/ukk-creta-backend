from rest_framework import serializers
from .models import Gerbong

class GerbongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gerbong
        fields = '__all__'