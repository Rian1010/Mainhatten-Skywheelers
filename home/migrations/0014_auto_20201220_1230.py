# Generated by Django 3.0 on 2020-12-20 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_remove_bannerbild_startseite_sektion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spieltabelle',
            name='startseite_sektion',
        ),
        migrations.AddField(
            model_name='spieltabelle',
            name='friendly_name',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
