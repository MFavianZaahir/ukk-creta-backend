# Generated by Django 5.1.5 on 2025-02-07 03:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kereta', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gerbong',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_gerbong', models.CharField(max_length=100)),
                ('kuota', models.IntegerField()),
                ('kereta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='gerbongs', to='kereta.kereta')),
            ],
        ),
    ]
