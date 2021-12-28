# Generated by Django 3.2.6 on 2021-12-28 01:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colleges',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('college_name', models.CharField(max_length=500, null=True, validators=[django.core.validators.MinLengthValidator(2)])),
                ('college_location', models.CharField(max_length=200, null=True)),
                ('college_level', models.CharField(max_length=200, null=True)),
                ('college_type', models.CharField(max_length=200, null=True)),
                ('college_popularity', models.CharField(max_length=200, null=True)),
                ('college_annual_cost', models.IntegerField()),
                ('college_image', models.FileField(null=True, upload_to='static/uploads')),
            ],
        ),
        migrations.DeleteModel(
            name='College',
        ),
    ]
