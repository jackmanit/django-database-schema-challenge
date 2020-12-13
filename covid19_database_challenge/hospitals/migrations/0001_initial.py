# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-12-13 08:35
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('city', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HospitalWorker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(choices=[('Doctor', 'Doctor'), ('Nurse', 'Nurse')], db_index=True, max_length=255)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_workers', to='hospitals.Department')),
            ],
        ),
        migrations.CreateModel(
            name='MedicalExaminationResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('result', models.CharField(choices=[('Healthy', 'Healthy'), ('Corona', 'Corona'), ('Botism', 'Botism'), ('Dead', 'Dead')], db_index=True, max_length=255)),
                ('examined_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_examination_results', to='hospitals.HospitalWorker')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients_details', to='hospitals.Department')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=6)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patients_details', to='hospitals.Person'),
        ),
        migrations.AddField(
            model_name='medicalexaminationresult',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='medical_examination_results', to='hospitals.Patient'),
        ),
        migrations.AddField(
            model_name='hospitalworker',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hospital_jobs', to='hospitals.Person'),
        ),
        migrations.AddField(
            model_name='department',
            name='hospital',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departments', to='hospitals.Hospital'),
        ),
    ]
