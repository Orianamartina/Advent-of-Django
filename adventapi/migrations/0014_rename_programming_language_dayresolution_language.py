# Generated by Django 5.0 on 2024-01-17 19:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("adventapi", "0013_language_remove_dayresolution_language_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="dayresolution",
            old_name="programming_language",
            new_name="language",
        ),
    ]
