from django.contrib import admin

from .models.agent import Agent
from .models.chairman import Chairman
from .models.employee import Resme
from .models.vacancy import Vacancy
from .models.volunteer import Resume


class ChairmanAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "position", "photo", "phone")
    list_display_links = ("id", "first_name")
    search_fields = ("first_name", "last_name", "position", "phone")
    date_hierarchy = 'created_at'


admin.site.register(Chairman, ChairmanAdmin)


class AgentAdmin(admin.ModelAdmin):
    list_display = ("id", "first_name", "last_name", "position", "photo", "phone")
    list_display_links = ("id", "first_name")
    search_fields = ("first_name", "last_name", "position", "phone")
    date_hierarchy = 'created_at'
    list_filter = ("country",)


admin.site.register(Agent, AgentAdmin)


class ResmeAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "file", "vacancy")
    list_display_links = ("id", "full_name")
    search_fields = ("first_name", "phone")
    date_hierarchy = 'created_at'
    list_filter = ("vacancy",)


admin.site.register(Resme, ResmeAdmin)


class VacancyAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "phone", "salary", "address", "work_volume")
    list_display_links = ("id", "title")
    search_fields = ("address", "salary", "title", "phone")
    date_hierarchy = 'created_at'


admin.site.register(Vacancy, VacancyAdmin)


class ResumeAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", "phone", "file", "vacancy", "email")
    list_display_links = ("id", "full_name")
    search_fields = ("first_name", "phone")
    date_hierarchy = 'created_at'
    list_filter = ("vacancy",)


admin.site.register(Resume, ResumeAdmin)
