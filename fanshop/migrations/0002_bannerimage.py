# Generated by Django 3.0 on 2020-11-23 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanshop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(default='', max_length=100)),
                ('banner', models.ImageField(upload_to='')),
            ],
        ),
    ]
