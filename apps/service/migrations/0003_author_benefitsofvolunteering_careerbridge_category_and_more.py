# Generated by Django 4.1.7 on 2023-03-06 13:09

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0005_instapost_url'),
        ('service', '0002_country_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('first_name', models.CharField(max_length=30, verbose_name='First name')),
                ('first_name_en', models.CharField(max_length=30, null=True, verbose_name='First name')),
                ('first_name_uz', models.CharField(max_length=30, null=True, verbose_name='First name')),
                ('first_name_ru', models.CharField(max_length=30, null=True, verbose_name='First name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last name')),
                ('last_name_en', models.CharField(max_length=30, null=True, verbose_name='Last name')),
                ('last_name_uz', models.CharField(max_length=30, null=True, verbose_name='Last name')),
                ('last_name_ru', models.CharField(max_length=30, null=True, verbose_name='Last name')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('position_en', models.CharField(max_length=100, null=True, verbose_name='Position')),
                ('position_uz', models.CharField(max_length=100, null=True, verbose_name='Position')),
                ('position_ru', models.CharField(max_length=100, null=True, verbose_name='Position')),
                ('photo', models.ImageField(upload_to='user', verbose_name='Photo')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('bio', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bio')),
                ('bio_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bio')),
                ('bio_uz', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bio')),
                ('bio_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Bio')),
                ('task', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Task')),
                ('task_en', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Task')),
                ('task_uz', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Task')),
                ('task_ru', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='Task')),
            ],
            options={
                'verbose_name': 'Author',
                'verbose_name_plural': 'Authors',
            },
        ),
        migrations.CreateModel(
            name='BenefitsOfVolunteering',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('icon', models.ImageField(upload_to='Icon', verbose_name='Icon')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
            ],
            options={
                'verbose_name': 'Benifits of volunteering',
                'verbose_name_plural': 'Benifits of volunteerings',
            },
        ),
        migrations.CreateModel(
            name='CareerBridge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('title_en', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_uz', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('title_ru', models.CharField(max_length=255, null=True, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('photo', models.ImageField(upload_to='event/%Y/%m/%d/', verbose_name='Photo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('content_en', ckeditor.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_uz', ckeditor.fields.RichTextField(null=True, verbose_name='Content')),
                ('content_ru', ckeditor.fields.RichTextField(null=True, verbose_name='Content')),
                ('ips', models.GenericIPAddressField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('video_link', models.CharField(max_length=255, verbose_name='Video link')),
            ],
            options={
                'verbose_name': 'Career',
                'verbose_name_plural': 'Careers',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('name_en', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_uz', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('name_ru', models.CharField(max_length=50, null=True, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Book category',
                'verbose_name_plural': 'Book categories',
            },
        ),
        migrations.CreateModel(
            name='Festival',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('photo', models.ImageField(upload_to='event/%Y/%m/%d/', verbose_name='Photo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('ips', models.GenericIPAddressField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Festival',
                'verbose_name_plural': 'Festivals',
            },
        ),
        migrations.CreateModel(
            name='ForVolunteer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('photo', models.ImageField(upload_to='event/%Y/%m/%d/', verbose_name='Photo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('ips', models.GenericIPAddressField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'For Volunteer',
                'verbose_name_plural': 'For Volunteers',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('photo', models.ImageField(upload_to='galery/%Y/%m/%d/', verbose_name='Photo')),
            ],
            options={
                'verbose_name': 'Gallery',
                'verbose_name_plural': 'Galleries',
            },
        ),
        migrations.CreateModel(
            name='Help',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('photo', models.ImageField(upload_to='event/%Y/%m/%d/', verbose_name='Photo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('ips', models.GenericIPAddressField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Gratuitous Help',
                'verbose_name_plural': 'Gratuitous Helps',
            },
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('name_en', models.CharField(max_length=30, null=True, verbose_name='name')),
                ('name_uz', models.CharField(max_length=30, null=True, verbose_name='name')),
                ('name_ru', models.CharField(max_length=30, null=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'Language',
                'verbose_name_plural': 'Languages',
            },
        ),
        migrations.CreateModel(
            name='Law',
            fields=[
                ('countrybase_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='common.countrybase')),
                ('file', models.FileField(upload_to='lwa/%Y/%m/%d/', verbose_name='File')),
            ],
            options={
                'verbose_name': 'Law',
                'verbose_name_plural': 'Laws',
            },
            bases=('common.countrybase',),
        ),
        migrations.CreateModel(
            name='Partnership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('photo', models.ImageField(upload_to='partner', verbose_name='Photo')),
                ('domain', models.CharField(max_length=50, verbose_name='Domain')),
                ('link', models.CharField(max_length=100, verbose_name='Link')),
            ],
            options={
                'verbose_name': 'Partnership',
                'verbose_name_plural': 'Partnerships',
            },
        ),
        migrations.CreateModel(
            name='RightAndObligation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('photo', models.ImageField(upload_to='event/%Y/%m/%d/', verbose_name='Photo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('ips', models.GenericIPAddressField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Right And Obligation',
                'verbose_name_plural': 'Right And Obligations',
            },
        ),
        migrations.CreateModel(
            name='StudyingAbroad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('photo', models.ImageField(upload_to='event/%Y/%m/%d/', verbose_name='Photo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('ips', models.GenericIPAddressField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Studying Abroad',
                'verbose_name_plural': 'Studying Abroads',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('name', models.CharField(max_length=50, verbose_name='Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'verbose_name': 'Tag',
                'verbose_name_plural': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Insurance',
            fields=[
                ('law_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='service.law')),
            ],
            options={
                'verbose_name': 'Insurance',
                'verbose_name_plural': 'Insurances',
            },
            bases=('service.law',),
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('full_name', models.CharField(max_length=100, verbose_name='Full name')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
                ('file', models.FileField(upload_to='resume/%Y/%m/%d/', verbose_name='File')),
                ('career', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='career_resumes', to='service.careerbridge', verbose_name='Career')),
            ],
            options={
                'verbose_name': 'Resume',
                'verbose_name_plural': 'Resumes',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('photo', models.ImageField(upload_to='event/%Y/%m/%d/', verbose_name='Photo')),
                ('content', ckeditor.fields.RichTextField(verbose_name='Content')),
                ('ips', models.GenericIPAddressField(blank=True, null=True)),
                ('views', models.IntegerField(default=0)),
                ('year', models.IntegerField(default=2020, verbose_name='Year')),
                ('page', models.IntegerField(default=300, verbose_name='Page')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='library_author', to='service.author', verbose_name='Author')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='library_category', to='service.category', verbose_name='Category')),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='service.language', verbose_name='Language')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update at')),
                ('question', models.TextField(verbose_name='Question')),
                ('answer', ckeditor.fields.RichTextField(verbose_name='Answer')),
                ('tag', models.ManyToManyField(to='service.tag', verbose_name='Tag')),
            ],
            options={
                'verbose_name': 'FAQ',
                'verbose_name_plural': 'FAQs',
            },
        ),
    ]