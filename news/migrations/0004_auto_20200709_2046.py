# Generated by Django 3.0 on 2020-07-09 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200708_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsheadlines',
            name='paragraph10',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='newsheadlines',
            name='paragraph8',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='newsheadlines',
            name='paragraph9',
            field=models.TextField(default=''),
        ),
    ]
