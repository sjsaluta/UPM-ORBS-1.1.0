# Generated by Django 4.0.4 on 2022-12-29 02:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0016_booking_date_picked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.DateTimeField(null=True),
        ),
    ]
