from django.utils.translation import gettext as _
from apps.common.models import ContentBase, ResumeBase, BaseModel
from django.db import models


class CareerBridge(ContentBase):
    video_link = models.CharField(verbose_name=_('Video link'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Career')
        verbose_name_plural = _('Careers')


class Resume(ResumeBase):
    career = models.ForeignKey(CareerBridge, verbose_name=_('Career'), on_delete=models.CASCADE,
                               related_name='career_resumes')

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = _('Resume')
        verbose_name_plural = _('Resumes')


class Gallery(BaseModel):
    photo = models.ImageField(upload_to='galery/%Y/%m/%d/', verbose_name='Photo')

    def __str__(self):
        return (self.id)

    class Meta:
        verbose_name = _('Gallery')
        verbose_name_plural = _('Galleries')