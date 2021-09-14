# Generated by Django 3.2.4 on 2021-08-26 03:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_alter_listing_bathrooms'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='address2',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='bathrooms',
            field=models.IntegerField(),
        ),
    ]