# Generated by Django 3.0.1 on 2021-10-30 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audio',
            name='link',
        ),
        migrations.AlterField(
            model_name='audio',
            name='label',
            field=models.ImageField(upload_to='', verbose_name='Photo'),
        ),
    ]
