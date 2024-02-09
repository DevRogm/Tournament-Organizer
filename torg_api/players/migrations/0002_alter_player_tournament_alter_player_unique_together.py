# Generated by Django 5.0.2 on 2024-02-09 13:07

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
        ('tournaments', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='tournament',
            field=models.ManyToManyField(blank=True, related_name='players', to='tournaments.tournament'),
        ),
        migrations.AlterUniqueTogether(
            name='player',
            unique_together={('organizer', 'name')},
        ),
    ]
