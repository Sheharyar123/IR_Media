from django.shortcuts import render
from django.views.generic import ListView
from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "course_list"
    paginate_by = 9

    def get_queryset(self):
        return Course.objects.filter(is_active=True)
