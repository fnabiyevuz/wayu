from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import ResumeBase
from .vacancy import Vacancy


class Resme(ResumeBase):
    vacancy = models.ForeignKey(Vacancy, verbose_name=_('Vacancy'), related_name='vacancy_voluntrs', on_delete=models.CASCADE)

    def __str__(self):
        return str(self.phone)

    class Meta:
        verbose_name = _('Resume')
        verbose_name_plural = _('Resumes')
