# Generated by Django 3.2.6 on 2021-08-23 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meetups', '0002_auto_20210823_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetup',
            old_name='judulKonten',
            new_name='jenisKonten',
        ),
    ]