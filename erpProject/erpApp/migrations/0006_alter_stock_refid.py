# Generated by Django 5.0 on 2024-01-06 13:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("erpApp", "0005_remove_product_purchase_orders_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="stock",
            name="refid",
            field=models.IntegerField(default=0),
        ),
    ]
