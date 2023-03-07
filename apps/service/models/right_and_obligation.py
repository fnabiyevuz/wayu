from django.utils.translation import gettext as _
from apps.common.models import ContentBase


class RightAndObligation(ContentBase):

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Right And Obligation')
        verbose_name_plural = _('Right And Obligations')
