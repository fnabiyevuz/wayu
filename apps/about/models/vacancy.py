from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import ContentBase


class Vacancy(ContentBase):
    address = models.CharField(verbose_name=_('Address'), max_length=150)
    salary = models.CharField(verbose_name=_('Salary'), max_length=30)
    phone = models.CharField(verbose_name=_('Phone'), max_length=15)
    work_volume = models.CharField(verbose_name=_('Work wolume'), max_length=30)

    def __str__(self):
        return self.address

    class Meta:
        verbose_name = _("Vacancy")
        verbose_name_plural = _("Vacancies")