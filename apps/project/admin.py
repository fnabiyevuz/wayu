from django.contrib import admin
from .models import *


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name", "about", "all_document_text")
    date_hierarchy = 'created_at'


admin.site.register(Project, ProjectAdmin)


class MessageAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "email", 'msg')
    list_display_links = ("id", "name")
    search_fields = ("name", "email", "msg")
    date_hierarchy = 'created_at'


admin.site.register(Message, MessageAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "title")
    list_display_links = ("id", "project")
    search_fields = ("project", "title")
    date_hierarchy = 'created_at'


admin.site.register(Task, TaskAdmin)


class DocumentAdmin(admin.ModelAdmin):
    list_display = ("id", "project", "file")
    list_display_links = ("id", "project")
    search_fields = ("project", "file")
    date_hierarchy = 'created_at'


admin.site.register(Document, DocumentAdmin)


class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", 'position', 'phone', 'email')
    list_display_links = ("id", "first_name")
    search_fields = ("first_name", "last_name", 'position', 'phone', 'email')
    date_hierarchy = 'created_at'
    list_filter = ('project',)


admin.site.register(TeamMember, TeamMemberAdmin)
