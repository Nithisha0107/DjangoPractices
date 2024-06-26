# Generated by Django 5.0 on 2024-01-09 13:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("App", "0002_remove_openingstock_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="StockReport",
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
                ("description", models.TextField()),
                ("stock_reference_id", models.IntegerField()),
                ("type", models.CharField(max_length=255)),
                ("stock", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="App.product"
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="Stock",
        ),
    ]
