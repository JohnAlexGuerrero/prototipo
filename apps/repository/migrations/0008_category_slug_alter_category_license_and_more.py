# Generated by Django 5.0.4 on 2024-04-30 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0007_software_origin_country_software_type_of_work_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='qarnx'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='category',
            name='license',
            field=models.CharField(blank=True, choices=[('PROPIETARIO', 'Software propietario'), ('CÓDIGO ABIERTO', 'Software de Código Abierto')], max_length=150, null=True, verbose_name='tipo de licencia'),
        ),
        migrations.AlterField(
            model_name='category',
            name='type_software',
            field=models.CharField(blank=True, choices=[('Software de productividad', 'Productivity'), ('Software de multimedia', 'Multimedia'), ('Juegos', 'Games'), ('Internet', 'Internet'), ('Herramientas', 'Tools'), ('Herramientas de desarrollo', 'Programacion'), ('Lenguaje de programación', 'Lenguajes De Programacion'), ('Herramientas Devops', 'Devops'), ('Bases de datos', 'Bases De Datos')], max_length=150, null=True, verbose_name='Tipo de software'),
        ),
    ]
