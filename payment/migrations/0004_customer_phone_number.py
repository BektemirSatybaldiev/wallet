# Generated by Django 4.1.7 on 2023-03-01 14:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0003_balance'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phone_number',
            field=models.CharField(blank=True, max_length=12, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '123456789012'. Up to 12 digits allowed.", regex='^996\\d{9}$')]),
        ),
    ]
