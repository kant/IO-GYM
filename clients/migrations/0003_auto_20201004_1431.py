# Generated by Django 3.1.1 on 2020-10-04 14:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0002_auto_20201001_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='clients',
            name='rfid_id',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Llave de acceso'),
        ),
        migrations.AlterField(
            model_name='memberships',
            name='expiration_date',
            field=models.DateField(choices=[(datetime.date(2020, 10, 3), 'Cancelado'), (datetime.date(2020, 10, 4), 'Visita (solo hoy)'), (datetime.date(2020, 10, 11), '1 semana'), (datetime.date(2020, 11, 3), '1 mes'), (datetime.date(2021, 1, 2), '3 meses'), (datetime.date(2021, 4, 2), '6 meses'), (datetime.date(2021, 10, 4), '1 año')], default=datetime.date(2020, 10, 4), verbose_name='Duración'),
        ),
    ]
