# Generated by Django 4.1.7 on 2023-03-03 12:29

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chairman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('photo', models.ImageField(upload_to='user', verbose_name='Photo')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bio')),
                ('task', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bio')),
            ],
            options={
                'verbose_name': 'Chairman',
                'verbose_name_plural': 'Chairmen',
            },
        ),
    ]
