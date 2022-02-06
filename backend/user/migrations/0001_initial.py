# Generated by Django 4.0 on 2022-01-23 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserProfile",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=255)),
                ("title", models.CharField(max_length=255)),
                ("location", models.CharField(max_length=255)),
                ("desired_location", models.CharField(max_length=255)),
                ("desired_salary", models.IntegerField()),
                ("about", models.TextField()),
                ("work_experience", models.JSONField()),
                ("skills_technologies", models.JSONField()),
                ("education", models.JSONField()),
                ("license_certification", models.JSONField()),
                ("languages", models.JSONField()),
            ],
        ),
    ]