# Generated by Django 4.2.7 on 2023-12-08 07:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modelApp", "0005_remove_employee_phone_number_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="email_id",
            field=models.CharField(
                max_length=250, validators=[django.core.validators.EmailValidator]
            ),
        ),
    ]
