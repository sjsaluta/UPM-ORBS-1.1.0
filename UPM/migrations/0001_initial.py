# Generated by Django 4.0.4 on 2023-01-17 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='College',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=300, null=True)),
                ('mobile_number', models.CharField(max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Equipment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True, unique=True)),
                ('slug', models.SlugField(null=True)),
                ('capacity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, null=True, unique=True)),
                ('slug', models.SlugField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('faculty', models.CharField(max_length=200, null=True)),
                ('coursetitle', models.CharField(max_length=200, null=True)),
                ('classnum', models.IntegerField(null=True, unique=True)),
                ('component', models.CharField(max_length=10, null=True)),
                ('section', models.CharField(max_length=10, null=True)),
                ('subject', models.CharField(max_length=200, null=True)),
                ('capacity', models.IntegerField(null=True)),
                ('time_start', models.TimeField(null=True)),
                ('time_end', models.TimeField(null=True)),
                ('dayofweek', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Term',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('academicyear', models.CharField(max_length=10)),
                ('semester', models.CharField(choices=[('1st SEMESTER', '1st Semester'), ('2nd SEMESTER', '2nd Semester'), ('MIDYEAR', 'midyear')], max_length=50, null=True)),
                ('slug', models.SlugField(null=True)),
                ('date_start', models.DateField(null=True)),
                ('date_end', models.DateField(null=True)),
                ('isActivated', models.BooleanField(default=False, null=True)),
                ('room', models.ManyToManyField(blank=True, related_name='room_term', to='UPM.room')),
            ],
        ),
        migrations.CreateModel(
            name='ScheduleFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
                ('college', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='UPM.college')),
            ],
        ),
    ]
