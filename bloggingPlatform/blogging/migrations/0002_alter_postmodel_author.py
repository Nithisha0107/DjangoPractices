# Generated by Django 5.0 on 2024-01-03 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("blogging", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postmodel",
            name="author",
            field=models.CharField(max_length=100),
        ),
    ]
