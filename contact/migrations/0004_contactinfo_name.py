# Generated by Django 3.0 on 2020-12-20 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_auto_20200901_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
