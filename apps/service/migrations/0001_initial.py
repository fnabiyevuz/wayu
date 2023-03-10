# Generated by Django 4.1.7 on 2023-03-04 06:04

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('common', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('countrybase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.countrybase')),
            ],
            options={
                'abstract': False,
            },
            bases=('common.countrybase',),
        ),
        migrations.CreateModel(
            name='Embassy',
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
                ('task', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Task')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='country_embassies', to='service.country', verbose_name='Country')),
            ],
            options={
                'verbose_name': 'Embassy',
                'verbose_name_plural': 'Embassies',
            },
        ),
    ]
