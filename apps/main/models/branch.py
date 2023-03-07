from apps.about.models.chairman import Chairman
from apps.common.models import BaseModel
from django.db import models
from django.utils.translation import gettext as _
# from phonenumber_field.modelfields import PhoneNumberField


class Branch(BaseModel):
    address = models.CharField(verbose_name=_('Address'), max_length=255)
    staff = models.OneToOneField(Chairman, verbose_name=_('Staff'), on_delete=models.CASCADE)
    email = models.EmailField(verbose_name=_('Email'), max_length=50)
    # phone = PhoneNumberField(verbose_name=_('Phone'), blank=True)
    phone = models.CharField(verbose_name=_('Phone'), max_length=15)
    latitude = models.DecimalField(verbose_name=_('Latitude'), max_digits=9, decimal_places=6)
    longitude = models.DecimalField(verbose_name=_('Longitude'), max_digits=9, decimal_places=6)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = 'Branch'
        verbose_name_plural = 'Branches'