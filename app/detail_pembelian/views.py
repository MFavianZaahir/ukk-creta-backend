from rest_framework import viewsets
from .models import DetailPembelian
from .serializers import DetailPembelianSerializer
from core.permissions import IsPelanggan, IsPetugas

# Create your views here.
class DetailPembelianViewSet(viewsets.ModelViewSet):
    queryset = DetailPembelian.objects.all()
    serializer_class = DetailPembelianSerializer
    permission_classes = [IsPelanggan | IsPetugas]
