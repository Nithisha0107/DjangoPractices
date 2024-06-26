# Generated by Django 4.2.7 on 2023-12-18 10:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("modelApp", "0006_alter_daily_atendance_check_in_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="daily_atendance",
            name="check_in",
            field=models.TimeField(default=datetime.time(15, 42, 29, 876773)),
        ),
        migrations.AlterField(
            model_name="daily_atendance",
            name="check_out",
            field=models.TimeField(default=datetime.time(15, 42, 29, 876773)),
        ),
        migrations.AlterField(
            model_name="daily_atendance",
            name="employee_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="modelApp.employee"
            ),
        ),
        migrations.AlterUniqueTogether(
            name="employee",
            unique_together={("email_id", "first_name")},
        ),
    ]
