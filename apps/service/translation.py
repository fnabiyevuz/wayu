from modeltranslation.translator import translator, TranslationOptions

from apps.service.models.career_bridge import CareerBridge
from apps.service.models.e_library import Author, Category, Language
from apps.service.models.embassy import Embassy, Country
from apps.service.models.faq import Tag, Faq
from apps.service.models.festival import Festival
from apps.service.models.for_volunteer import ForVolunteer, BenefitsOfVolunteering
from apps.service.models.gratuitous_help import Help
from apps.service.models.insurance import Insurance
from apps.service.models.migration_law import Law
from apps.service.models.partner import Partnership
from apps.service.models.right_and_obligation import RightAndObligation
from apps.service.models.studying_abroad import StudyingAbroad


class CareerBridgeTranslationOptions(TranslationOptions):
    fields = ('title', 'content')


translator.register(CareerBridge, CareerBridgeTranslationOptions)


class LanguageTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Language, LanguageTranslationOptions)


class CategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Category, CategoryTranslationOptions)


class AuthorTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'position', 'bio', 'task',)


translator.register(Author, AuthorTranslationOptions)


# class CountryTranslationOptions(TranslationOptions):
#     fields = ('name', 'about')
#
#
# translator.register(Country, CountryTranslationOptions)
#

# class EmbassyTranslationOptions(TranslationOptions):
#     fields = ('first_name', 'last_name', 'position', 'bio', 'task')
#
#
# translator.register(Embassy, EmbassyTranslationOptions)
#
#
# class TagTranslationOptions(TranslationOptions):
#     fields = ('name',)
#
#
# translator.register(Tag, TagTranslationOptions)
#
#
# class FaqTranslationOptions(TranslationOptions):
#     fields = ('question', 'answer')
#
#
# translator.register(Faq, FaqTranslationOptions)
#
#
# class FestivalTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')
#
#
# translator.register(Festival, FestivalTranslationOptions)
#
#
# class ForVolunteerTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')
#
#
# translator.register(ForVolunteer, ForVolunteerTranslationOptions)
#
#
# class BenefitsOfVolunteeringTranslationOptions(TranslationOptions):
#     fields = ('title',)
#
#
# translator.register(BenefitsOfVolunteering, BenefitsOfVolunteeringTranslationOptions)
#
#
# class HelpTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')
#
#
# translator.register(Help, HelpTranslationOptions)


# class InsuranceTranslationOptions(TranslationOptions):
#     fields = ('name',)
#
#
# translator.register(Insurance, InsuranceTranslationOptions)
#
#
# class LawTranslationOptions(TranslationOptions):
#     fields = ('name',)
#
#
# translator.register(Law, LawTranslationOptions)
#
#
# class PartnershipTranslationOptions(TranslationOptions):
#     fields = ('title',)
#
#
# translator.register(Partnership, PartnershipTranslationOptions)
#
#
# class RightAndObligationTranslationOptions(TranslationOptions):
#     fields = ('title', 'content',)
#
#
# translator.register(RightAndObligation, RightAndObligationTranslationOptions)
#
#
# class StudyingAbroadTranslationOptions(TranslationOptions):
#     fields = ('title', 'content',)
#
#
# translator.register(StudyingAbroad, StudyingAbroadTranslationOptions)
