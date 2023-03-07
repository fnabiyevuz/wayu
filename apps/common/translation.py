from modeltranslation.translator import translator, TranslationOptions

from .models import CategoryBase, TagBase, ContentBase, UserBase, ResumeBase, CountryBase, Region


# class CategoryBaseTranslationOptions(TranslationOptions):
#     fields = ('name',)
#
#
# translator.register(CategoryBase, CategoryBaseTranslationOptions)

# class TagBaseTranslationOptions(TranslationOptions):
#     fields = ('name',)
#
#
# translator.register(TagBase, TagBaseTranslationOptions)
#

# class ContentBaseTranslationOptions(TranslationOptions):
#     fields = ('title', 'content')
#
#
# translator.register(ContentBase, ContentBaseTranslationOptions)


# class UserBaseTranslationOptions(TranslationOptions):
#     fields = ('first_name', 'last_name', 'position', 'bio', 'task')
#
#
# translator.register(UserBase, UserBaseTranslationOptions)


# class ResumeBaseTranslationOptions(TranslationOptions):
#     fields = ('full_name',)
#
#
# translator.register(ResumeBase, ResumeBaseTranslationOptions)
#
#
# class CountryBaseTranslationOptions(TranslationOptions):
#     fields = ('full_name',)
#
#
# translator.register(CountryBase, CountryBaseTranslationOptions)
#
#
# class RegionTranslationOptions(TranslationOptions):
#     fields = ('full_name',)
#
#
# translator.register(Region, RegionTranslationOptions)
#
