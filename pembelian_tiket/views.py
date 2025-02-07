from rest_framework.response import Response
from rest_framework.decorators import action
from .models import PembelianTiket
from .serializers import PembelianTiketSerializer
from rest_framework import viewsets
from knox_project.permissions import IsPelanggan, IsPetugas
from datetime import datetime
from django.db.models import Sum

class PembelianTiketViewSet(viewsets.ModelViewSet):
    queryset = PembelianTiket.objects.all()
    serializer_class = PembelianTiketSerializer

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [IsPelanggan | IsPetugas]
        else:
            permission_classes = [IsPelanggan]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['get'])
    def monthly_report(self, request):
        month = request.query_params.get('month', datetime.now().month)
        year = request.query_params.get('year', datetime.now().year)
        
        total = self.queryset.filter(
            tanggal_pembelian__year=year,
            tanggal_pembelian__month=month
        ).aggregate(
            total=Sum('jadwal__harga')
        )['total'] or 0

        return Response({
            'month': month,
            'year': year,
            'total_income': total
        })