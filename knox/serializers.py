from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.contrib.auth.models import User
from django.db import transaction
from app.petugas.models import Petugas
from app.pelanggan.models import Pelanggan

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'role')
        

class SignupSerializer(serializers.ModelSerializer):
    role = serializers.ChoiceField(choices=[('petugas', 'Petugas'), ('pelanggan', 'Pelanggan')], default='pelanggan')
    nama_petugas = serializers.CharField(max_length=100, required=False)
    nik = serializers.CharField(max_length=100, required=False)
    nama_penumpang = serializers.CharField(max_length=100, required=False)
    alamat = serializers.CharField(required=False)
    telp = serializers.CharField(max_length=20, required=False)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'role', 'nama_petugas', 'nik', 'nama_penumpang', 'alamat', 'telp']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        if data['role'] == 'pelanggan':
            required_fields = ['nik', 'nama_penumpang', 'alamat', 'telp']
        elif data['role'] == 'petugas':
            required_fields = ['nama_petugas', 'alamat', 'telp']
        else:
            required_fields = []

        for field in required_fields:
            if not data.get(field):
                raise serializers.ValidationError(f"{field} is required for {data['role']} registration")

        return data

    def create(self, validated_data):
        role = validated_data.pop('role')
        nama_petugas = validated_data.pop('nama_petugas', None)
        alamat = validated_data.pop('alamat', None)
        telp = validated_data.pop('telp', None)

        with transaction.atomic():
            user = User.objects.create_user(**validated_data)
            user.role = role
            user.save()

            if role == 'pelanggan':
                    pelanggan_data = {
                        'NIK': validated_data.pop('nik', None),
                        'nama_penumpang': validated_data.pop('nama_penumpang', None),
                        'alamat': validated_data.pop('alamat', None),
                        'telp': validated_data.pop('telp', None),
                    }
                    Pelanggan.objects.create(user=user, **pelanggan_data)
            elif role == 'petugas':
                    petugas_data = {
                        'nama_petugas': nama_petugas,
                        'alamat': alamat,
                        'telp': telp,
                    }
                    Petugas.objects.create(user=user, **petugas_data)

        return user
    
class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'role')