# Generated by Django 5.0 on 2024-01-17 19:44

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("adventapi", "0011_dayresolution_link_to_repo"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Reply",
            new_name="Comment",
        ),
    ]