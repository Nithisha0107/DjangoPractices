# Generated by Django 5.0 on 2024-01-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("todoApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="Created_at",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]