# Generated by Django 4.0 on 2022-02-18 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0005_alter_jobposting_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobposting',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
