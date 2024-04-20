# Generated by Django 5.0.4 on 2024-04-20 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0003_alter_requeriment_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='software',
            name='license',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Propietario'), (2, 'Libre'), (3, 'Código Abierto')], default=2, verbose_name='tipo de licencia'),
        ),
    ]
