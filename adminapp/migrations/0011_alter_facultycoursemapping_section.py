# Generated by Django 5.1.4 on 2025-01-13 06:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_facultycoursemapping_component_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultycoursemapping',
            name='section',
            field=models.IntegerField(default=1),
        ),
    ]
