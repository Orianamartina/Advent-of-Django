# Generated by Django 5.0 on 2024-01-05 19:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("adventapi", "0002_dayresolution_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="dayresolution",
            name="code",
            field=models.CharField(default="null", max_length=1000),
            preserve_default=False,
        ),
    ]