# Generated by Django 5.0.4 on 2024-04-07 03:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Software',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Software titulo')),
                ('description', models.TextField(max_length=250, verbose_name='descripción')),
                ('version', models.CharField(max_length=50, verbose_name='version')),
                ('license', models.PositiveSmallIntegerField(choices=[(1, 'Propietario'), (2, 'Libre'), (3, 'Código Abierto')], default=1, verbose_name='tipo de licencia')),
                ('slug', models.SlugField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'Software',
                'verbose_name_plural': 'Softwares',
            },
        ),
    ]
