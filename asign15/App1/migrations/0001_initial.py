# Generated by Django 4.2.7 on 2023-12-14 13:57

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Entrepreneur",
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
                ("name", models.CharField(max_length=200)),
                ("company_name", models.CharField(max_length=100)),
                ("img_path", models.CharField(max_length=100)),
            ],
        ),
    ]
