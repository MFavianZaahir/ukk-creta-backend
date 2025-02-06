from django.urls import path

from knox import views

urlpatterns = [
    path(r'signup/', views.SignupView.as_view(), name='knox_signup'),
    path(r'login/', views.LoginView.as_view(), name='knox_login'),
    path(r'logout/', views.LogoutView.as_view(), name='knox_logout'),
    path(r'logoutall/', views.LogoutAllView.as_view(), name='knox_logoutall'),
]
