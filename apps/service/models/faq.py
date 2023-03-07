from django.db import models
from django.utils.translation import gettext as _
from apps.common.models import BaseModel, TagBase
from ckeditor.fields import RichTextField


class Tag(TagBase):
    pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Tag')
        verbose_name_plural = _('Tags')


class Faq(BaseModel):
    question = models.TextField(verbose_name=_('Question'))
    answer = RichTextField(verbose_name=_('Answer'))
    tag = models.ManyToManyField(Tag, verbose_name=_("Tag"))

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = _('FAQ')
        verbose_name_plural = _('FAQs')
