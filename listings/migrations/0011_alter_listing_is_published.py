# Generated by Django 3.2.4 on 2021-10-06 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_listing_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]