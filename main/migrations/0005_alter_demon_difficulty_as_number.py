# Generated by Django 4.2.2 on 2023-06-26 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_difficulty_options_alter_nationality_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demon',
            name='difficulty_as_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
