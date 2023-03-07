from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import UserBase, CountryBase
from ckeditor.fields import RichTextField


class Country(CountryBase):
    about = RichTextField(verbose_name=_('About'))


class Embassy(UserBase):
    country = models.ForeignKey(Country, verbose_name=_('Country'), on_delete=models.PROTECT,
                                related_name='country_embassies')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Embassy')
        verbose_name_plural = _('Embassies')
