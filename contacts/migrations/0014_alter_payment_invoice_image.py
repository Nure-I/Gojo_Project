# Generated by Django 3.2.4 on 2021-10-07 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0013_payment_invoice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment_invoice',
            name='image',
            field=models.ImageField(upload_to='invoice'),
        ),
    ]
