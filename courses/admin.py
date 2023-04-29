from django.contrib import admin
from .models import Instructor, Course, Student, UserCourse


class UserCourseAdmin(admin.TabularInline):
    model = UserCourse
    readonly_fields = ["user", "course", "purchase_date"]
    extra = 0


class CourseAdmin(admin.ModelAdmin):
    list_display = ["title", "price", "category", "duration", "language", "is_active"]
    inlines = [UserCourseAdmin]
    prepopulated_fields = {"slug": ("title",)}
    list_editable = ["is_active"]
    search_fields = ["title", "category"]


admin.site.register(Instructor)
admin.site.register(Course, CourseAdmin)
admin.site.register(Student)
