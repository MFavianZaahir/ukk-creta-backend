from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from .views import RootView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('knox.urls')),
    path('api/', RootView.as_view(), name="api-root"),
    path('pelanggan/', include('pelanggan.urls')),
    path('petugas/', include('petugas.urls')),
    path('kereta/', include('kereta.urls')),
    path('gerbong/', include('gerbong.urls')),
    path('kursi/', include('kursi.urls')),
    path('jadwal/', include('jadwal.urls')),
    path('tiket/', include('pembelian_tiket.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)