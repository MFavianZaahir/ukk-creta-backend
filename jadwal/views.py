from rest_framework import viewsets
from .models import Jadwal
from .serializers import JadwalSerializer
from knox_project.permissions import IsPetugas, IsPelanggan

# Create your views here.
class JadwalViewSet(viewsets.ModelViewSet):
    queryset = Jadwal.objects.all()
    serializer_class = JadwalSerializer
    permission_classes = [IsPetugas]

class JadwalListView(viewsets.ReadOnlyModelViewSet):
    queryset = Jadwal.objects.all()
    serializer_class = JadwalSerializer
    permission_classes = [IsPelanggan]

    def get_queryset(self):
        queryset = super().get_queryset()
        # Add any filtering logic here
        return queryset