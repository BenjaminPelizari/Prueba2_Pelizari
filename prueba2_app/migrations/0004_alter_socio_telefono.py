# Generated by Django 4.2.4 on 2023-11-29 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prueba2_app', '0003_alter_socio_telefono'),
    ]

    operations = [
        migrations.AlterField(
            model_name='socio',
            name='telefono',
            field=models.CharField(max_length=15),
        ),
    ]
