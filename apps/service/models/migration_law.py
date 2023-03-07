from django.utils.translation import gettext as _
from apps.common.models import CountryBase
from django.db import models


class Law(CountryBase):
    file = models.FileField(verbose_name=_('File'), upload_to='lwa/%Y/%m/%d/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Law')
        verbose_name_plural = _('Laws')
