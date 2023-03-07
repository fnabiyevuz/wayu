from django.contrib import admin

from apps.common.models import InstaPost, CountryBase, Region

admin.site.register(InstaPost)
admin.site.register(CountryBase)
admin.site.register(Region)