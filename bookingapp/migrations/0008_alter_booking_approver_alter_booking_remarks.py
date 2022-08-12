# Generated by Django 4.0.4 on 2022-08-10 05:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_adpd_college_alter_ao_college'),
        ('bookingapp', '0007_alter_booking_isapproved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='approver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.adpd'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='remarks',
            field=models.TextField(null=True),
        ),
    ]
