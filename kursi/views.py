from rest_framework import viewsets
from .models import Kursi
from .serializers import KursiSerializer
from knox_project .permissions import IsPetugas

# Create your views here.
class KursiViewSet(viewsets.ModelViewSet):
    queryset = Kursi.objects.all()
    serializer_class = KursiSerializer
    permission_classes = [IsPetugas]
