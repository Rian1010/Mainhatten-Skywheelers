# Generated by Django 3.0 on 2020-12-13 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20200704_1740'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bannerbild',
            name='startseite_sektion',
        ),
    ]