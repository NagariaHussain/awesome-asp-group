# Generated by Django 4.0 on 2022-01-13 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("recruiting", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jobposting",
            name="is_published",
            field=models.BooleanField(default=False),
        ),
    ]
