# Generated by Django 3.2.4 on 2021-09-09 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_contact_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='status',
        ),
        migrations.AddField(
            model_name='contact',
            name='requested',
            field=models.BooleanField(default=False),
        ),
    ]
