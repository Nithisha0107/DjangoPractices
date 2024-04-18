# Generated by Django 5.0 on 2024-01-06 07:02

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("erpApp", "0004_alter_product_purchase_orders_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="product",
            name="purchase_orders",
        ),
        migrations.RemoveField(
            model_name="product",
            name="sales_orders",
        ),
        migrations.AddField(
            model_name="openingstock",
            name="created",
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="purchaseorder",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name="salesorder",
            name="created",
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.CreateModel(
            name="ProductPurchase",
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
                ("stock", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="erpApp.product"
                    ),
                ),
                (
                    "purchase",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="erpApp.purchaseorder",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ProductSales",
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
                ("stock", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="erpApp.product"
                    ),
                ),
                (
                    "purchase",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="erpApp.salesorder",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Stock",
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
                ("refid", models.IntegerField()),
                ("type", models.CharField(max_length=100)),
                ("stock", models.IntegerField()),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="erpApp.product"
                    ),
                ),
            ],
        ),
    ]