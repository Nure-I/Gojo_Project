# Generated by Django 3.2.4 on 2021-08-26 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20210826_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='address2',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]