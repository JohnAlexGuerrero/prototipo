# Generated by Django 5.0.4 on 2024-04-18 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0009_customuser_second_last_name_alter_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'Hombre'), (2, 'Mujer')], null=True),
        ),
    ]
