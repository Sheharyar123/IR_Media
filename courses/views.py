from typing import Any, Optional
from django.db import models
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView
from .models import Course


class CourseListView(ListView):
    model = Course
    template_name = "courses/course_list.html"
    context_object_name = "course_list"
    paginate_by = 9

    def get_queryset(self):
        return Course.objects.filter(is_active=True)


class CourseDetailView(DetailView):
    model = Course
    template_name = "courses/course_detail.html"
    context_object_name = "course"

    def get_object(self):
        course = get_object_or_404(
            Course, slug=self.kwargs.get("course_slug"), is_active=True
        )
        return course
