from django.db import models
from app.gerbong.models import Gerbong

# Create your models here.
class Kursi(models.Model):
    gerbong = models.ForeignKey(Gerbong, on_delete=models.CASCADE, related_name="kursis")  # One-to-Many: A train car has many seats
    no_kursi = models.CharField(max_length=10)

    def __str__(self):
        return f"Kursi {self.no_kursi} - {self.gerbong.nama_gerbong}"