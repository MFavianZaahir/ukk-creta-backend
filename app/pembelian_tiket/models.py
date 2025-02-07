from django.db import models
from app.pelanggan.models import Pelanggan
from app.jadwal.models import Jadwal

# Create your models here.
class PembelianTiket(models.Model):
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE, related_name="pembelians")  # One-to-Many: A customer can have multiple ticket purchases
    jadwal = models.ForeignKey(Jadwal, on_delete=models.CASCADE, related_name="pembelians")  # One-to-Many: A schedule can have many ticket purchases
    tanggal_pembelian = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tiket {self.pelanggan.nama_penumpang} - {self.jadwal.kereta.nama_kereta}"