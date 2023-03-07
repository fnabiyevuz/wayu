from apps.common.models import BaseModel
from django.db import models
from django.utils.translation import gettext as _


class Link(BaseModel):
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='useful link')
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    domain = models.CharField(verbose_name=_('Domain'), max_length=50)
    url = models.CharField(verbose_name=_('Link'), max_length=255)