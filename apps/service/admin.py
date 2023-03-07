from django.contrib import admin

from .models.career_bridge import CareerBridge
from .models.embassy import Embassy
from .models.for_volunteer import ForVolunteer, BenefitsOfVolunteering
from .models.gratuitous_help import Help
from .models.insurance import Insurance
from .models.internship import Intern
from .models.migration_law import Law
from .models.partner import Partnership
from .models.right_and_obligation import RightAndObligation
from .models.studying_abroad import StudyingAbroad


class CareerBridgeAdmin(admin.ModelAdmin):
    list_display = ("id", "title", 'video_link')
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    date_hierarchy = 'created_at'


admin.site.register(CareerBridge, CareerBridgeAdmin)


class ForVolunteerAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    date_hierarchy = 'created_at'


admin.site.register(ForVolunteer, ForVolunteerAdmin)


class BenefitsOfVolunteeringAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "icon")
    list_display_links = ("id", "title")
    search_fields = ("title",)
    date_hierarchy = 'created_at'


admin.site.register(BenefitsOfVolunteering, BenefitsOfVolunteeringAdmin)


class HelpAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    date_hierarchy = 'created_at'


admin.site.register(Help, HelpAdmin)


class InsuranceAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'file')
    list_display_links = ("id", "name")
    search_fields = ("name",)
    date_hierarchy = 'created_at'


admin.site.register(Insurance, InsuranceAdmin)


class InternAdmin(admin.ModelAdmin):
    list_display = ("id", "full_name", 'region', 'phone', 'university', 'faculty')
    list_display_links = ("id", "full_name")
    search_fields = ("full_name",)
    date_hierarchy = 'created_at'
    list_filter = ('region',)


admin.site.register(Intern, InternAdmin)


class LawAdmin(admin.ModelAdmin):
    list_display = ("id", "name", 'file')
    list_display_links = ("id", "name")
    search_fields = ("name",)
    date_hierarchy = 'created_at'


admin.site.register(Law, LawAdmin)


class PartnershipAdmin(admin.ModelAdmin):
    list_display = ("id", "title", 'domain', 'link')
    list_display_links = ("id", "title")
    search_fields = ("title",)
    date_hierarchy = 'created_at'


admin.site.register(Partnership, PartnershipAdmin)


class RightAndObligationAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    date_hierarchy = 'created_at'


admin.site.register(RightAndObligation, RightAndObligationAdmin)


class StudyingAbroadAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    date_hierarchy = 'created_at'


admin.site.register(StudyingAbroad, StudyingAbroadAdmin)
