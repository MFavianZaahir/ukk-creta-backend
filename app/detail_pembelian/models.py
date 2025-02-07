from django.db import models
from app.pembelian_tiket.models import PembelianTiket
from app.kursi.models import Kursi

# Create your models here.
class DetailPembelian(models.Model):
    pembelian_tiket = models.ForeignKey(PembelianTiket, on_delete=models.CASCADE, related_name="detail_pembelians")  # One-to-Many: A ticket purchase can have multiple details
    kursi = models.ForeignKey(Kursi, on_delete=models.CASCADE, related_name="detail_pembelians")  # One-to-Many: A seat can be assigned to multiple purchases
    NIK = models.CharField(max_length=100)
    nama_penumpang = models.CharField(max_length=100)

    def __str__(self):
        return f"Detail for {self.nama_penumpang} - {self.kursi.no_kursi}"