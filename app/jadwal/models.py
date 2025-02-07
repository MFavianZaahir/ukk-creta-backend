from django.db import models
from app.kereta.models import Kereta

# Create your models here.
class Jadwal(models.Model):
    kereta = models.ForeignKey(Kereta, on_delete=models.CASCADE, related_name="jadwals")
    asal_keberangkatan = models.CharField(max_length=100)
    tujuan_keberangkatan = models.CharField(max_length=100)
    tanggal_berangkat = models.DateTimeField()
    tanggal_kedatangan = models.DateTimeField()
    harga = models.FloatField()

    def __str__(self):
        return f"{self.asal_keberangkatan} to {self.tujuan_keberangkatan} - {self.kereta.nama_kereta}"