# Generated by Django 4.1.7 on 2023-03-06 08:29

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='about',
            field=ckeditor.fields.RichTextField(default=1, verbose_name='About'),
            preserve_default=False,
        ),
    ]
