from rest_framework import viewsets
from .models import Kereta
from .serializers import KeretaSerializer
from app.core.permissions import IsPetugas

# Create your views here.
class KeretaViewSet(viewsets.ModelViewSet):
    queryset = Kereta.objects.all()
    serializer_class = KeretaSerializer
    permission_classes = [IsPetugas]