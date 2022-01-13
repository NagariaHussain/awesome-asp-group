from django.contrib import admin
from django.urls import path, re_path, include
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

vue_router = never_cache(TemplateView.as_view(template_name="index.html"))

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("recruiting.api.urls")),
    # All remaining routes are handled by Vue SPA's router
    re_path(r"^(?!admin|api|media|static|assets|ws).*$", vue_router, name="vuejs"),
]
