from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel


class Partnership(BaseModel):
    title = models.CharField(verbose_name=_('Title'), max_length=255)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='partner')
    domain = models.CharField(verbose_name=_('Domain'), max_length=50)
    link = models.CharField(verbose_name=_('Link'), max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Partnership')
        verbose_name_plural = _('Partnerships')