# Generated by Django 3.2.4 on 2021-09-27 03:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0010_listing_owner'),
        ('contacts', '0007_contactus'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(default='Not Payed', max_length=100)),
                ('payment_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='contacts.contact')),
                ('house', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='listings.listing')),
            ],
        ),
    ]
