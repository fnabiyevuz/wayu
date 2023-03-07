from django.contrib import admin

from .models.branch import Branch
from .models.contribute import Contribute
from .models.feedback import Messages
from .models.news import CategoryNews, Tag, News
from .models.scheduledevent import Category, Event
from .models.useful_link import Link


class BranchAdmin(admin.ModelAdmin):
    list_display = ("id", "address", "staff", "email", "phone")
    list_display_links = ("id", "address")
    search_fields = ("address", "last_name", "position", "phone")
    date_hierarchy = 'created_at'


admin.site.register(Branch, BranchAdmin)


class ContributeAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "donation", "payment_type")
    list_display_links = ("id", "name")
    search_fields = ("name", "donation")
    date_hierarchy = 'created_at'
    list_filter = ('payment_type',)


admin.site.register(Contribute, ContributeAdmin)


class MessagesAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "email", "msg")
    list_display_links = ("id", "name")
    search_fields = ("name", "phone", "email")
    date_hierarchy = 'created_at'


admin.site.register(Messages, MessagesAdmin)


class CategoryNewsAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    date_hierarchy = 'created_at'
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(CategoryNews, CategoryNewsAdmin)


class TagAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    date_hierarchy = 'created_at'
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Tag, TagAdmin)


class NewsAdmin(admin.ModelAdmin):
    list_display = ("id", "title",)
    list_display_links = ("id", "title")
    search_fields = ("title",)
    date_hierarchy = 'created_at'
    list_filter = ("category",)
    filter_horizontal = ("tag",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(News, NewsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    date_hierarchy = 'created_at'


admin.site.register(Category, CategoryAdmin)


class EventAdmin(admin.ModelAdmin):
    list_display = ("id", "title", 'scheduled_date')
    list_display_links = ("id", "title")
    search_fields = ("title",)
    date_hierarchy = 'created_at'
    list_filter = ('category',)


admin.site.register(Event, EventAdmin)


class LinkAdmin(admin.ModelAdmin):
    list_display = ("id", "title", 'domain', 'url')
    list_display_links = ("id", "title")
    search_fields = ("title", 'domain')
    date_hierarchy = 'created_at'


admin.site.register(Link, LinkAdmin)
