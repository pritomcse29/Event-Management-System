# Generated by Django 5.1.6 on 2025-02-20 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0004_alter_category_description_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255),
        ),
    ]
