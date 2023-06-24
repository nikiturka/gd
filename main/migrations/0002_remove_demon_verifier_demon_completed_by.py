# Generated by Django 4.2.2 on 2023-06-24 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='demon',
            name='verifier',
        ),
        migrations.AddField(
            model_name='demon',
            name='completed_by',
            field=models.ManyToManyField(to='main.player'),
        ),
    ]
