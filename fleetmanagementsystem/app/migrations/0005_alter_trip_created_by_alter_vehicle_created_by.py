# Generated by Django 5.0 on 2024-02-05 04:51

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0004_alter_trip_created_by_alter_vehicle_created_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trip",
            name="created_by",
            field=models.IntegerField(default=1, null=True),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="created_by",
            field=models.IntegerField(default=1, null=True),
        ),
    ]
