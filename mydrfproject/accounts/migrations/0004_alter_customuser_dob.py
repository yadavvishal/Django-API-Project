# Generated by Django 5.0.3 on 2024-04-04 20:19

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_createdat_customuser_dob_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dob',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
