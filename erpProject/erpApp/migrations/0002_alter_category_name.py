# Generated by Django 5.0 on 2024-01-05 09:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("erpApp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="category",
            name="name",
            field=models.CharField(max_length=250, unique=True),
        ),
    ]