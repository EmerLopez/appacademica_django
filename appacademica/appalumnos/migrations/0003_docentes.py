# Generated by Django 4.2.6 on 2023-11-03 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appalumnos', '0002_materia'),
    ]

    operations = [
        migrations.CreateModel(
            name='docentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=65)),
                ('telefono', models.CharField(max_length=9)),
            ],
        ),
    ]
