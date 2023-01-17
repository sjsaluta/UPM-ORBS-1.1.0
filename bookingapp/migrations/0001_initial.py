# Generated by Django 4.0.4 on 2023-01-17 17:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
        ('UPM', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dept_or_office', models.CharField(blank=True, max_length=300, null=True)),
                ('organization', models.CharField(blank=True, max_length=300, null=True)),
                ('subject', models.CharField(blank=True, max_length=300, null=True)),
                ('activity', models.CharField(max_length=300, null=True)),
                ('isApproved', models.BooleanField(blank=True, null=True)),
                ('isEdited', models.BooleanField(blank=True, null=True)),
                ('date_approved', models.DateField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField(null=True)),
                ('end_time', models.DateTimeField(null=True)),
                ('numofstudents', models.IntegerField(null=True)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('approver', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.adpd')),
                ('booker', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('equipment', models.ManyToManyField(to='UPM.equipment')),
                ('faculty', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.faculty')),
                ('room', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.room')),
            ],
        ),
    ]
