from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from app.core.views import RootView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('knox.urls')),
    path('api/', RootView.as_view(), name="api-root"),
    path('pelanggan/', include('app.pelanggan.urls')),
    path('petugas/', include('app.petugas.urls')),
    path('kereta/', include('app.kereta.urls')),
    path('gerbong/', include('app.gerbong.urls')),
    path('kursi/', include('app.kursi.urls')),
    path('jadwal/', include('app.jadwal.urls')),
    path('tiket/', include('app.pembelian_tiket.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)