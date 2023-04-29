from django.contrib import admin
from .models import Instructor, Course, Student


class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "category", "duration", "language", "is_active"]
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ["is_active"]
    search_fields = ["title", "category"]


admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
