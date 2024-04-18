# Generated by Django 5.0 on 2024-02-05 06:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_alter_trip_updated_by_alter_vehicle_updated_by"),
    ]

    operations = [
        migrations.AlterField(
            model_name="trip",
            name="created_by",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="trip",
            name="updated_by",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="created_by",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="vehicle",
            name="updated_by",
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]