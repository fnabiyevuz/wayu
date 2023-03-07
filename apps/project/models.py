from apps.common.models import BaseModel, MessageBase, UserBase
from django.db import models
from django.utils.translation import gettext as _
from ckeditor.fields import RichTextField


class Project(BaseModel):
    name = models.CharField(verbose_name=_('Name'), max_length=100)
    photo = models.ImageField(verbose_name=_('Photo'), upload_to='project')
    about = RichTextField(verbose_name=_('About project'))
    all_document_text = models.TextField(verbose_name=_('All document text'))


class Message(MessageBase):
    pass

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Message'
        verbose_name_plural = 'Messages'


class Task(BaseModel):
    project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='project_tsks',
                                on_delete=models.PROTECT)
    icon = models.ImageField(verbose_name=_('icon'), upload_to='task')
    title = models.CharField(verbose_name=_('Title'), max_length=50)
    text = models.TextField(verbose_name=_('Text'))

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'


class Document(BaseModel):
    project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='project_tasks',
                                on_delete=models.PROTECT)
    file = models.FileField(verbose_name=_('File'), upload_to='project')

    def __str__(self):
        return self.project.name + "'s file"

    class Meta:
        verbose_name = 'Document'
        verbose_name_plural = 'Documents'


class TeamMember(UserBase):
    project = models.ForeignKey(Project, verbose_name=_('Project'), related_name='project_members',
                                on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Team Member'
        verbose_name_plural = 'Team Members'
