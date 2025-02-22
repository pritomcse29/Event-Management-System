# Generated by Django 5.1.6 on 2025-02-19 15:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='events.category'),
        ),
        migrations.AddField(
            model_name='participant',
            name='event',
            field=models.ManyToManyField(related_name='event', to='events.event'),
        ),
    ]
