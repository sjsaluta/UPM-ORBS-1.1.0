# Generated by Django 4.0.4 on 2022-08-10 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookingapp', '0008_alter_booking_approver_alter_booking_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
