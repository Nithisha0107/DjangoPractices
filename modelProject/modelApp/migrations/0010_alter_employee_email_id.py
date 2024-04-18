# Generated by Django 4.2.7 on 2023-12-08 08:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("modelApp", "0009_alter_employee_email_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="email_id",
            field=models.CharField(
                max_length=100, validators=[django.core.validators.EmailValidator]
            ),
        ),
    ]
