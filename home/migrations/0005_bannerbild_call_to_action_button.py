# Generated by Django 3.0 on 2020-07-03 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20200703_1711'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerbild',
            name='call_to_action_button',
            field=models.CharField(default='', max_length=20),
        ),
    ]
