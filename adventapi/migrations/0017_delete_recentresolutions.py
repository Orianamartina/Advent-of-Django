# Generated by Django 5.0 on 2024-01-22 20:09

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("adventapi", "0016_remove_dayresolution_day_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="RecentResolutions",
        ),
    ]
