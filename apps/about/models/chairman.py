from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import UserBase


class Chairman(UserBase):
    work_schedule = models.CharField(max_length=100, verbose_name=_('Work schedule'))

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Chairman')
        verbose_name_plural = _('Chairmen')
