from apps.common.models import BaseModel, MessageBase
from django.db import models
from django.utils.translation import gettext as _


class Messages(MessageBase):
    phone = models.CharField(verbose_name=_('Phone'), max_length=15)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'
