from django.db import models
from django.conf import settings

class Petugas(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="petugas")
    nama_petugas = models.CharField(max_length=100)
    alamat = models.TextField()
    telp = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_petugas