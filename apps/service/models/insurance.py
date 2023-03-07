from django.utils.translation import gettext as _
from .migration_law import Law


class Insurance(Law):
    pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Insurance')
        verbose_name_plural = _('Insurances')