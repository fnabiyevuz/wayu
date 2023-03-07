from django.utils.translation import gettext as _
from apps.common.models import BaseModel, ContentBase, UserBase, CategoryBase
from django.db import models


class Language(BaseModel):
    name = models.CharField(verbose_name=_('name'), max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Language')
        verbose_name_plural = _('Languages')


class Category(CategoryBase):
    pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Book category')
        verbose_name_plural = _('Book categories')


class Author(UserBase):
    pass

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Library(ContentBase):
    author = models.ForeignKey(Author, verbose_name=_('Author'), on_delete=models.CASCADE,
                               related_name="library_author")
    category = models.ForeignKey(Category, verbose_name=_('Category'), on_delete=models.CASCADE,
                                 related_name="library_category")
    year = models.IntegerField(verbose_name=_('Year'), default=2020)
    page = models.IntegerField(verbose_name=_('Page'), default=300)
    language = models.ForeignKey(Language, verbose_name=_('Language'), on_delete=models.PROTECT)