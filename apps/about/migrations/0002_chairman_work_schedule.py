# Generated by Django 4.1.7 on 2023-03-03 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chairman',
            name='work_schedule',
            field=models.CharField(default=1, max_length=100, verbose_name='Work schedule'),
            preserve_default=False,
        ),
    ]