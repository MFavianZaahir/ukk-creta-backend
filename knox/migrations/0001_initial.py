# Generated by Django 5.1.5 on 2025-02-04 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthToken',
            fields=[
                ('digest', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('token_key', models.CharField(db_index=True, max_length=25)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expiry', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'swappable': 'KNOX_TOKEN_MODEL',
            },
        ),
    ]
