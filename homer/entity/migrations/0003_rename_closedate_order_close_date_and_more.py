# Generated by Django 5.0.2 on 2024-03-03 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('entity', '0002_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='closeDate',
            new_name='close_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='creationDate',
            new_name='creation_date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='startDate',
            new_name='start_date',
        ),
    ]
