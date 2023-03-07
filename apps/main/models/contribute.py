from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import BaseModel
from ..choices import PaymentType


class Contribute(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=25)
    donation = models.DecimalField(verbose_name=_('Donation'), decimal_places=2, max_digits=9)
    payment_type = models.CharField(max_length=5, choices=PaymentType.choices, default=PaymentType.PAYME)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contribute'
        verbose_name_plural = 'Contributes'
