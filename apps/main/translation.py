from modeltranslation.translator import translator, TranslationOptions

from .models.branch import Branch
from .models.contribute import Contribute
from .models.news import News
from .models.scheduledevent import Event
from .models.useful_link import Link


class BranchTranslationOptions(TranslationOptions):
    fields = ('address',)


translator.register(Branch, BranchTranslationOptions)



class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(News, NewsTranslationOptions)


class EventTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(Event, EventTranslationOptions)


class LinkTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Link, LinkTranslationOptions)
