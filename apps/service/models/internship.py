from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel, Region


class TimeType(models.TextChoices):
    YES = "Да, смогу"
    NO = "Нет, только на половину дня"
    OTHER = "Другое"


class ContinueType(models.TextChoices):
    FULL_DAY = "Полный день"
    PART_TIME = "Неполный рабочий день"
    ONLY_SUMMER = "Нет, только на летний период"
    OTHER = "Другое"


class Intern(BaseModel):
    full_name = models.CharField(verbose_name=_('Full name'), max_length=100)
    birthday = models.DateField(verbose_name=_('Region'))
    region = models.ForeignKey(Region, verbose_name=_('Region'), on_delete=models.PROTECT,
                               related_name='region_interns')
    email = models.EmailField(verbose_name=_('Email'))
    phone = models.CharField(verbose_name=_('Phone'), max_length=15)
    activity = models.CharField(verbose_name=_('Activity'), max_length=50)
    start_date = models.DateField(verbose_name=_('Start date'))
    time = models.CharField(max_length=30, choices=TimeType.choices, default=TimeType.YES)
    continues = models.CharField(max_length=30, choices=ContinueType.choices, default=ContinueType.PART_TIME)
    university = models.CharField(verbose_name=_('Education'), max_length=150)
    faculty = models.CharField(verbose_name=_('Faculty'), max_length=150)
    enter_year = models.IntegerField(verbose_name=_('Enter year'), default=2020)
    end_year = models.IntegerField(verbose_name=_('End year'), default=2020)
    gpa = models.DecimalField(verbose_name=_('GPA'), decimal_places=2, max_digits=5)
    experience = models.TextField(verbose_name=_('Experience'), )
    knowledge = models.TextField(verbose_name=_('Knowledge'), )
    resume = models.FileField(verbose_name=_('resume'), upload_to='intern_resume')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Intership in Uzbekistan')
        verbose_name_plural = _('Interships in Uzbekistan')
