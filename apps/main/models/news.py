from django.db import models
from django.utils.translation import gettext as _

from apps.common.models import BaseModel, CategoryBase, ContentBase, Region, TagBase


class CategoryNews(CategoryBase):
    pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'News Category'
        verbose_name_plural = 'News Categories'


class Tag(TagBase):
    pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'News Tag'
        verbose_name_plural = 'News Tags'


class News(ContentBase):
    category = models.ForeignKey(CategoryNews, verbose_name=_('Category News'), on_delete=models.PROTECT,
                                 related_name='category_news')
    tag = models.ManyToManyField(Tag, verbose_name=_('Category Tag'))
    region = models.ForeignKey(Region, verbose_name=_('Region'), related_name='news_region', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'News'
        verbose_name_plural = 'News'
