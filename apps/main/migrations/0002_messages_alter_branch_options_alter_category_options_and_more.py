# Generated by Django 4.1.7 on 2023-03-07 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('msg', models.TextField()),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
            ],
            options={
                'verbose_name': 'Message',
                'verbose_name_plural': 'Messages',
            },
        ),
        migrations.AlterModelOptions(
            name='branch',
            options={'verbose_name': 'Branch', 'verbose_name_plural': 'Branches'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': "Event's Category", 'verbose_name_plural': "Event's Categories"},
        ),
        migrations.AlterModelOptions(
            name='categorynews',
            options={'verbose_name': 'News Category', 'verbose_name_plural': 'News Categories'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'News Tag', 'verbose_name_plural': 'News Tags'},
        ),
    ]