# Generated by Django 2.0.5 on 2018-06-05 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ShortLinks', '0007_auto_20180521_1844'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shortlink',
            options={'ordering': ['-CreationDate']},
        ),
    ]
