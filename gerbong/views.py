from rest_framework import viewsets
from .models import Gerbong
from .serializers import GerbongSerializer
from knox_project.permissions import IsPetugas

# Create your views here.
class GerbongViewSet(viewsets.ModelViewSet):
    queryset = Gerbong.objects.all()
    serializer_class = GerbongSerializer
    permission_classes = [IsPetugas]