from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import ContentBase, CategoryBase


class Category(CategoryBase):
    pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Event's Category"
        verbose_name_plural = "Event's Categories"

class Event(ContentBase):
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.PROTECT,
                                 related_name='category_events')
    scheduled_date = models.DateTimeField(verbose_name=_('Scheduled date'))
    latitude = models.DecimalField(verbose_name=_('Latitude'), max_digits=9, decimal_places=6)
    longitude = models.DecimalField(verbose_name=_('Longitude'), max_digits=9, decimal_places=6)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Event'
        verbose_name_plural = 'Events'
