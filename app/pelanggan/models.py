from django.db import models
from django.conf import settings

class Pelanggan(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="pelanggan")
    NIK = models.CharField(max_length=100, unique=True, null=True, blank=True)
    nama_penumpang = models.CharField(max_length=100)
    alamat = models.TextField()
    telp = models.CharField(max_length=20)

    def __str__(self):
        return self.nama_penumpang
