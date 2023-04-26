from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("irmedia_admin/", admin.site.urls),
    path("", include("core.urls")),
    path("", include("blogs.urls")),
    path("projects/", include("projects.urls")),
    path("courses/", include("courses.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
