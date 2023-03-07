from modeltranslation.translator import translator, TranslationOptions
from .models.agent import Agent
from .models.chairman import Chairman
from .models.employee import Resme
from .models.vacancy import Vacancy
from .models.volunteer import Vacancy as vac


class AgentTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'position', 'bio', 'task')


translator.register(Agent, AgentTranslationOptions)


class ChairmanTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'position', 'bio', 'task')


translator.register(Chairman, ChairmanTranslationOptions)


class ResumeTranslationOptions(TranslationOptions):
    fields = ('full_name',)


translator.register(Resme, ResumeTranslationOptions)


class VacancyTranslationOptions(TranslationOptions):
    fields = ('address', 'work_volume')


translator.register(Vacancy, VacancyTranslationOptions)


# class vacTranslationOptions(TranslationOptions):
#     fields = ('full_name',)
#
#
# translator.register(vac, vacTranslationOptions)
