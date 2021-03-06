# Generated by Django 2.0.5 on 2018-05-21 13:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ShortLinks', '0004_auto_20180521_1613'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shortlink',
            old_name='User',
            new_name='CreatedBy',
        ),
        migrations.AlterField(
            model_name='shortlink',
            name='ExpirationDate',
            field=models.DateTimeField(default=datetime.datetime(2018, 5, 21, 13, 32, 14, 562226, tzinfo=utc), verbose_name='Expiration Date'),
        ),
    ]
