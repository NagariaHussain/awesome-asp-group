# Generated by Django 4.0 on 2022-03-11 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('recruiting', '0014_interviewround_index_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='communication',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
    ]
