# Generated by Django 5.1.4 on 2024-12-17 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0006_alter_faculty_designation_alter_faculty_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='department',
            field=models.CharField(choices=[('CSE(Regular)', 'CSE(R)'), ('CSE(HONORS)', 'CSE(H)'), ('CSE(IT)', 'CSIT'), ('ECE', 'ECE')], max_length=50),
        ),
    ]
