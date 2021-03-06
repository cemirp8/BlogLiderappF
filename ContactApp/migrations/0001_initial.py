# Generated by Django 4.0.4 on 2022-06-24 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DudaEstudiante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Interesado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.IntegerField()),
                ('curso_de_interes', models.CharField(max_length=30)),
            ],
        ),
    ]
