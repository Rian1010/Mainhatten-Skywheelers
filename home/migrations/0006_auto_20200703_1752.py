# Generated by Django 3.0 on 2020-07-03 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_bannerbild_call_to_action_button'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bannerbild',
            name='call_to_action_button',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='spieltabelle',
            name='datum',
            field=models.DateField(default=''),
        ),
    ]
