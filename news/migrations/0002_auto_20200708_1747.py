# Generated by Django 3.0 on 2020-07-08 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsheadlines',
            name='paragraph1',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='newsheadlines',
            name='second_heading',
            field=models.CharField(blank=True, default='', max_length=254, null=True),
        ),
    ]
