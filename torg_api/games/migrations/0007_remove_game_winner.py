# Generated by Django 5.0.2 on 2024-02-14 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0006_alter_game_winner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='winner',
        ),
    ]
