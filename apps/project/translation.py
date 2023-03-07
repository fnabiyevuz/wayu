from modeltranslation.translator import translator, TranslationOptions

from apps.project.models import Project, Task, TeamMember


class ProjectTranslationOptions(TranslationOptions):
    fields = ('name', 'about', 'all_document_text')


translator.register(Project, ProjectTranslationOptions)

class TaskTranslationOptions(TranslationOptions):
    fields = ('title', 'text')


translator.register(Task, TaskTranslationOptions)

class TeamMemberTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name', 'position', 'bio', 'task')


translator.register(TeamMember, TeamMemberTranslationOptions)
