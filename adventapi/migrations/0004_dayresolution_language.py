# Generated by Django 5.0 on 2024-01-05 20:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adventapi", "0003_dayresolution_code"),
    ]

    operations = [
        migrations.AddField(
            model_name="dayresolution",
            name="language",
            field=models.CharField(default="none", max_length=40),
            preserve_default=False,
        ),
    ]
