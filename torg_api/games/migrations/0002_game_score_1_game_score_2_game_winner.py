# Generated by Django 5.0.2 on 2024-02-09 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='score_1',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='score_2',
            field=models.IntegerField(default=None, null=True),
        ),
        migrations.AddField(
            model_name='game',
            name='winner',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]
