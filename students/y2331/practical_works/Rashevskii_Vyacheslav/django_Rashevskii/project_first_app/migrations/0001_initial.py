# Generated by Django 3.0.4 on 2020-03-24 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_plate', models.CharField(max_length=6)),
                ('brand', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('color', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('birth_date', models.DateField()),
                ('sex', models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('N', 'Unspecified')], max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Ownership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Car')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
        migrations.CreateModel(
            name='DriverLicense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('date', models.DateField()),
                ('type', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E')], max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='project_first_app.Owner')),
            ],
        ),
    ]
