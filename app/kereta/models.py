from django.db import models

# Create your models here.
class Kereta(models.Model):
    nama_kereta = models.CharField(max_length=100)
    deskripsi = models.TextField()
    kelas = models.CharField(max_length=50)

    def __str__(self):
        return self.nama_kereta