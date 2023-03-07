from django.utils.translation import gettext as _

from apps.common.models import ContentBase


class Help(ContentBase):
    pass

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Gratuitous Help')
        verbose_name_plural = _('Gratuitous Helps')
