# Generated by Django 4.1.2 on 2022-10-12 16:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0004_alter_doctor_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='patient',
            options={'verbose_name': 'Paciente', 'verbose_name_plural': 'Pacientes'},
        ),
    ]