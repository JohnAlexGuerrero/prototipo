# Generated by Django 5.0.4 on 2024-05-13 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repository', '0017_alter_software_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='thumbnail',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AlterField(
            model_name='category',
            name='type_software',
            field=models.CharField(blank=True, choices=[('Software de productividad ayuda a los usuarios a realizar tareas comunes de manera más eficiente.', 'Productividad'), ('Software de creatividad ayuda a los usuarios a crear contenido multimedia, como imágenes, videos y música.', 'Creatividad'), ('El software de comunicación ayuda a los usuarios a comunicarse con otros.', 'Comunicacion'), ('El software empresarial ayuda a las empresas a realizar sus operaciones.', 'Negocios'), ('El software de programación ayuda a los desarrolladores a crear distintas aplicaciones.', 'Programacion'), ('El software de entretenimiento ayuda a los usuarios a relajarse y divertirse.', 'Entretenimiento'), ('El software educativo ayuda a los usuarios a aprender cosas nuevas.', 'Educacion'), ('El software de bienestar se enfoca en el cuidado de la salud de los usuarios.', 'Bienestar Y Salud')], max_length=150, null=True, verbose_name='Tipo de software'),
        ),
        migrations.AlterField(
            model_name='software',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]
