# Generated by Django 5.0 on 2024-01-25 04:40

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("erpApp", "0009_remove_productpurchase_product_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="product_unque_num",
            new_name="unique_num",
        ),
    ]
