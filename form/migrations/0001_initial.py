# Generated by Django 3.2.9 on 2021-11-18 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='myModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('other_names', models.CharField(max_length=30)),
                ('a_k_a', models.CharField(max_length=20)),
                ('sex', models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=1)),
                ('age', models.CharField(choices=[('A', '<10'), ('B', '10 - 20'), ('C', '21 - 30')], max_length=1)),
                ('height', models.CharField(max_length=10)),
                ('date_declared_missing', models.DateField(auto_now_add=True)),
                ('image_upload', models.ImageField(blank=True, default='images/profile1.png', null=True, upload_to='images/')),
                ('last_known_address', models.CharField(max_length=40)),
                ('area', models.CharField(max_length=30)),
                ('city', models.CharField(max_length=30)),
                ('state', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('contact_name', models.CharField(max_length=40)),
                ('phone_number', models.CharField(max_length=11)),
                ('contact_person_email', models.CharField(max_length=30)),
                ('contact_person_address', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='youModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=40)),
            ],
        ),
    ]
