# Generated by Django 3.0 on 2020-07-11 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_auto_20200710_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='firstGalleryPageTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='secondGalleryPageTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='thirdGalleryPageTitle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page_title', models.CharField(default='', max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='firstgallerypage',
            name='page_title',
        ),
        migrations.RemoveField(
            model_name='secondgallerypage',
            name='page_title',
        ),
        migrations.RemoveField(
            model_name='thirdgallerypage',
            name='page_title',
        ),
        migrations.AlterField(
            model_name='firstgallerypage',
            name='image_column_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='firstgallerypage',
            name='image_column_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='firstgallerypage',
            name='image_column_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='firstgallerypage',
            name='image_column_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='secondgallerypage',
            name='image_column_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='secondgallerypage',
            name='image_column_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='secondgallerypage',
            name='image_column_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='secondgallerypage',
            name='image_column_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='thirdgallerypage',
            name='image_column_1',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='thirdgallerypage',
            name='image_column_2',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='thirdgallerypage',
            name='image_column_3',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='thirdgallerypage',
            name='image_column_4',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]