# Generated by Django 4.0 on 2022-03-13 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('recruiting', '0022_alter_interviewevent_interview_round_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='interviewfileattachment',
            name='uploader',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
    ]
