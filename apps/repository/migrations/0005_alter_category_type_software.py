# Generated by Django 5.0.4 on 2024-04-29 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0004_alter_category_type_industry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='type_software',
            field=models.TextField(blank=True, choices=[('Productividad', 'Software de productividad'), ('Multimedia', 'Software de multimedia'), ('Juegos', 'Juegos'), ('Internet', 'Internet'), ('Herramientas', 'Herramientas')], max_length=150, null=True, verbose_name='Tipo de software'),
        ),
    ]
