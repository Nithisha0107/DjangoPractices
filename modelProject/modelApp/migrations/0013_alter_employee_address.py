# Generated by Django 4.2.7 on 2023-12-08 09:12

import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):
    dependencies = [
        ("modelApp", "0012_alter_employee_email_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="employee",
            name="address",
            field=models.CharField(
                max_length=250,
                validators=[
                    django.core.validators.RegexValidator(
                        re.compile("^[-a-zA-Z0-9_]+\\Z"),
                        "Enter a valid “slug” consisting of letters, numbers, underscores or hyphens.",
                        "invalid",
                    )
                ],
            ),
        ),
    ]
