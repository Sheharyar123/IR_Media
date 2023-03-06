from django.contrib import admin
from .models import Project, Category


class ProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "is_active"]
    prepopulated_fields = {"slug": ("title",)}
    list_editable = [
        "is_active",
    ]
    ordering = ["-updated_on", "-created_on"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
