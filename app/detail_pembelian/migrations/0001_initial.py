# Generated by Django 5.1.5 on 2025-02-07 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DetailPembelian',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NIK', models.CharField(max_length=100)),
                ('nama_penumpang', models.CharField(max_length=100)),
            ],
        ),
    ]
