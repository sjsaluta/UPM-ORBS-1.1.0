# Generated by Django 4.0.4 on 2022-12-22 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0014_alter_booking_equipment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.TimeField(null=True),
        ),
    ]
