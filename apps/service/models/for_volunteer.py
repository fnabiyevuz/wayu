from django.utils.translation import gettext as _
from apps.common.models import ContentBase, BaseModel
from django.db import models


class ForVolunteer(ContentBase):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('For Volunteer Content')
        verbose_name_plural = _('For Volunteer Contents')


class BenefitsOfVolunteering(BaseModel):
    icon = models.ImageField(verbose_name=_('Icon'), upload_to='Icon')
    title = models.CharField(verbose_name=_('Title'), max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Benifits of volunteering')
        verbose_name_plural = _('Benifits of volunteerings')
