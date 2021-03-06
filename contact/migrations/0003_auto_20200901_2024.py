# Generated by Django 3.0 on 2020-09-01 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20200901_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='emailHeading',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='phoneHeading',
            field=models.CharField(blank=True, default='', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='email',
            field=models.EmailField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='phoneNumber',
            field=models.CharField(blank=True, default='', max_length=20, null=True),
        ),
    ]
