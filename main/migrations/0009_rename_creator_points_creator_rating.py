# Generated by Django 4.2.2 on 2023-06-28 18:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_rename_rating_creator_creator_points'),
    ]

    operations = [
        migrations.RenameField(
            model_name='creator',
            old_name='creator_points',
            new_name='rating',
        ),
    ]
