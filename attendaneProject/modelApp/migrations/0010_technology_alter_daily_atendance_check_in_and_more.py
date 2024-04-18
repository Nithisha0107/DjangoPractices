# Generated by Django 4.2.7 on 2023-12-18 13:13

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("modelApp", "0009_alter_daily_atendance_check_in_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Technology",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("domain", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="daily_atendance",
            name="check_in",
            field=models.TimeField(default=datetime.time(18, 43, 39, 294991)),
        ),
        migrations.AlterField(
            model_name="daily_atendance",
            name="check_out",
            field=models.TimeField(default=datetime.time(18, 43, 39, 294991)),
        ),
        migrations.AlterField(
            model_name="daily_atendance",
            name="employee_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.DO_NOTHING, to="modelApp.employee"
            ),
        ),
        migrations.CreateModel(
            name="Emp_Tech",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "emp_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="modelApp.employee",
                    ),
                ),
                (
                    "tech_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="modelApp.technology",
                    ),
                ),
            ],
        ),
    ]