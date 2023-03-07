from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls.static import static
from django.conf import settings
from apps.common.down import download_users_posts_with_periods
from apps.common.selen_new import web_scraping

urlpatterns = [
                  path('download_users_posts_with_periods/', download_users_posts_with_periods),
                  path('web_scraping', web_scraping),
                  path('admin/', admin.site.urls),
                  re_path(r'^rosetta/', include('rosetta.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
