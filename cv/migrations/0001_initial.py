# Generated by Django 2.0.6 on 2018-06-12 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courses_taken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Course', models.CharField(max_length=75)),
                ('Grade', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Institution', models.CharField(max_length=75)),
                ('Location', models.CharField(max_length=75)),
                ('Degree', models.CharField(max_length=75)),
                ('Course', models.CharField(max_length=75)),
                ('Grad', models.DateTimeField(verbose_name='Graduation Date')),
                ('Grades', models.DecimalField(decimal_places=3, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_name', models.CharField(max_length=100)),
                ('Description', models.CharField(max_length=300)),
                ('Technologies_used', models.CharField(max_length=300)),
            ],
        ),
    ]
