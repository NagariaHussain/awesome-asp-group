# Generated by Django 4.0 on 2022-03-06 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruiting', '0012_interviewfileattachment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interviewevent',
            name='interview',
        ),
        migrations.CreateModel(
            name='InterviewRound',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('interview', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruiting.interview')),
            ],
        ),
        migrations.AddField(
            model_name='interviewevent',
            name='interview_round',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recruiting.interviewround'),
        ),
    ]
