# Generated by Django 5.1.5 on 2025-02-07 03:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('jadwal', '0001_initial'),
        ('pelanggan', '0003_alter_pelanggan_nik'),
    ]

    operations = [
        migrations.CreateModel(
            name='PembelianTiket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_pembelian', models.DateTimeField(auto_now_add=True)),
                ('jadwal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pembelians', to='jadwal.jadwal')),
                ('pelanggan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pembelians', to='pelanggan.pelanggan')),
            ],
        ),
    ]
