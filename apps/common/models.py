from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField
# from phonenumber_field.modelfields import PhoneNumberField


class BaseModel(models.Model):
    created_at = models.DateTimeField(verbose_name=_('Created at'), auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name=_('Update at'), auto_now=True)

    class Meta:
        abstract = True


class CategoryBase(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    slug = models.SlugField(verbose_name=_('Slug'))

    class Meta:
        abstract = True


class TagBase(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    slug = models.SlugField(verbose_name=_('Slug'))

    class Meta:
        abstract = True


class ContentBase(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    slug = models.SlugField(verbose_name=_('Slug'))
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='event/%Y/%m/%d/')
    content = RichTextField(verbose_name=_('Content'))
    ips = models.GenericIPAddressField(null=True, blank=True)
    views = models.IntegerField(default=0)

    class Meta:
        abstract = True


class UserBase(BaseModel):
    first_name = models.CharField(verbose_name=_('First name'), max_length=30)
    last_name = models.CharField(verbose_name=_('Last name'), max_length=30)
    position = models.CharField(verbose_name=_('Position'), max_length=100)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='user')
    phone = models.CharField(verbose_name=_('Phone'), max_length=15)
    # phone = PhoneNumberField(null=True, blank=True)
    email = models.EmailField(verbose_name=_('Email'))
    bio = RichTextField(verbose_name=_('Bio'), null=True, blank=True)
    task = RichTextField(verbose_name=_('Task'), null=True, blank=True)

    class Meta:
        abstract = True


class ResumeBase(BaseModel):
    full_name = models.CharField(verbose_name=_('Full name'), max_length=100)
    phone = models.CharField(verbose_name=_('Phone'), max_length=15)
    # phone = PhoneNumberField(null=True, blank=True)
    file = models.FileField(verbose_name=_('File'), upload_to='resume/%Y/%m/%d/')

    class Meta:
        abstract = True


class MessageBase(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    email = models.EmailField(verbose_name=_('Email'))
    msg = models.TextField()

    class Meta:
        abstract = True


class CountryBase(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=50)
    flag = models.ImageField(verbose_name=_('Flag'), upload_to='flag')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')


class Region(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Region')
        verbose_name_plural = _('Regions')


class InstaPost(BaseModel):
    photo = models.ImageField(upload_to='instagram/%Y/%m/%d/')
    caption = models.TextField()
    url = models.CharField(max_length=255)

    def __str__(self):
        return self.caption

    class Meta:
        verbose_name = _('InstaPost')
        verbose_name_plural = _('InstaPosts')