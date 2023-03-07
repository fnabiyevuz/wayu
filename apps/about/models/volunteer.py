from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import ResumeBase
from .vacancy import Vacancy


class Resume(ResumeBase):
    email = models.EmailField(verbose_name=_('Email'), max_length=75)
    vacancy = models.ForeignKey(Vacancy, verbose_name=_('Vacancy'), related_name='vacancy_volunteers', on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _("Volunteer's Resume")
        verbose_name_plural = _("Volunteer's Resumes")