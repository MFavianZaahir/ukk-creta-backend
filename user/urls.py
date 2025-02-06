from django.urls import path
from user.views import ProfileUpdateView

urlpatterns = [
    path('profile/', ProfileUpdateView.as_view(), name='profile-update'),
]
