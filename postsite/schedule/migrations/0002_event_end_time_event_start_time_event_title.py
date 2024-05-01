# Generated by Django 5.0.3 on 2024-04-28 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]