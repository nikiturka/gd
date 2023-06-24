# Generated by Django 4.2.2 on 2023-06-24 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_demon_verifier_demon_completed_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='creator',
            name='position_in_rating',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='player',
            name='position_in_rating',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='player',
            name='rating',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
    ]
