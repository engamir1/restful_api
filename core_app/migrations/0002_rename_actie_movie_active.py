# Generated by Django 5.2.3 on 2025-06-15 18:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='actie',
            new_name='active',
        ),
    ]
