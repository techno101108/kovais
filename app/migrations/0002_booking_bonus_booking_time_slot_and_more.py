# Generated by Django 5.0.7 on 2024-10-07 13:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bonus',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.bonus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='time_slot',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='userdetails',
            name='subscribed',
            field=models.BooleanField(default=False),
        ),
    ]
