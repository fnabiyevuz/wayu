from django.utils.translation import gettext as _
from apps.common.models import ContentBase


class Festival(ContentBase):
    pass

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = _('Festival')
        verbose_name_plural = _('Festivals')
