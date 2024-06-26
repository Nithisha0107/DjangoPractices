# Generated by Django 4.2.7 on 2023-12-09 11:14

from django.db import migrations, models
import encryptApp.models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Student",
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
                ("name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=100)),
                ("std_id", models.IntegerField(default=-1)),
                ("test_val", models.IntegerField(default=23)),
                ("enc_field", encryptApp.models.EncryptedField()),
            ],
        ),
    ]
