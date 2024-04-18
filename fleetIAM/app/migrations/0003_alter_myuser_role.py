# Generated by Django 5.0 on 2024-02-07 04:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_role_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="myuser",
            name="role",
            field=models.ForeignKey(
                default=2, on_delete=django.db.models.deletion.PROTECT, to="app.role"
            ),
        ),
    ]