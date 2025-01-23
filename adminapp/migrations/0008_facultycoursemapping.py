# Generated by Django 5.1.4 on 2025-01-09 06:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0007_alter_faculty_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facultycoursemapping',
            fields=[
                ('mapping_id', models.AutoField(primary_key=True, serialize=False)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.course')),
                ('faculty', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.faculty')),
            ],
            options={
                'db_table': 'facultycoursemapping_table',
            },
        ),
    ]
