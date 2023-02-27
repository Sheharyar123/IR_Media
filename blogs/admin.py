from django.contrib import admin
from .models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ["user", "subject", "is_active"]
    list_editable = [
        "is_active",
    ]
    list_filter = [
        "is_active",
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
