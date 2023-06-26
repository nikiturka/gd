# Generated by Django 4.2.2 on 2023-06-26 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_creator_position_in_rating_player_position_in_rating_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='difficulty',
            options={'verbose_name_plural': 'Difficulties'},
        ),
        migrations.AlterModelOptions(
            name='nationality',
            options={'verbose_name_plural': 'Nationalities'},
        ),
        migrations.AlterField(
            model_name='demon',
            name='difficulty_as_number',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=7, null=True),
        ),
    ]