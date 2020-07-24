# Generated by Django 3.0 on 2020-07-07 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPageBannerPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='SportsHallInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptor', models.CharField(default='', max_length=40)),
                ('description', models.CharField(default='', max_length=40)),
                ('training_day', models.CharField(blank=True, default='', max_length=40, null=True)),
                ('training_time', models.CharField(blank=True, default='', max_length=40, null=True)),
            ],
        ),
    ]