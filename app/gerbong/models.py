from django.db import models
from app.kereta.models import Kereta

# Create your models here.
class Gerbong(models.Model):
    kereta = models.ForeignKey(Kereta, on_delete=models.CASCADE, related_name="gerbongs")  # One-to-Many: A train has many train cars
    nama_gerbong = models.CharField(max_length=100)
    kuota = models.IntegerField()

    def __str__(self):
        return f"{self.nama_gerbong} - {self.kereta.nama_kereta}"