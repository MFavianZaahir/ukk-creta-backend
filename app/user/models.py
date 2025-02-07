from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = [
        ('petugas', 'Petugas'),
        ('pelanggan', 'Pelanggan'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='pelanggan')
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='custom_user_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='custom_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
