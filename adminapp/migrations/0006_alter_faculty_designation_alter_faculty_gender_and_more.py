# Generated by Django 5.1.4 on 2024-12-17 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0005_alter_course_academicyear'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='designation',
            field=models.CharField(choices=[('M.Tech.', 'M.Tech.'), ('Ph.D.', 'Ph.D.')], max_length=50),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='qualification',
            field=models.CharField(choices=[('Prof.', 'Professor'), ('Assoc. Prof', 'Associate Professor'), ('Asst. Prof', 'Assistant Professor')], max_length=30),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(choices=[('CSE(Regular)', 'CSE(R)'), ('CSE(HONORS)', 'CSE(H)'), ('CSE(IT)', 'CSIT'), ('ECE', 'ECE')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Others', 'Others')], max_length=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='program',
            field=models.CharField(choices=[('B.Tech.', 'B.Tech.'), ('M.Tech.', 'M.Tech.')], max_length=50),
        ),
        migrations.AlterField(
            model_name='student',
            name='semester',
            field=models.CharField(choices=[('Even', 'Even'), ('Odd', 'Odd')], max_length=10),
        ),
    ]
