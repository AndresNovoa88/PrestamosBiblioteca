# Generated by Django 4.1 on 2022-09-23 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionPrestamos', '0003_alter_prestamo_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devolution',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateField(auto_now=True)),
                ('prestamo', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='gestionPrestamos.prestamo')),
            ],
        ),
    ]
