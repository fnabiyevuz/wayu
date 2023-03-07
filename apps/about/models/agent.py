from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import BaseModel, UserBase, CountryBase


class Agent(UserBase):
    country = models.ForeignKey(CountryBase, verbose_name=_('Country'), on_delete=models.CASCADE,
                                related_name='country_agents')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Agent')
        verbose_name_plural = _('Agents')
