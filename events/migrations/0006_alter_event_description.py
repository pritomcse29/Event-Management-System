# Generated by Django 5.1.6 on 2025-02-20 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
