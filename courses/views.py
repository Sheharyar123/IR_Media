from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, View
from payments.models import Payment
from .models import Course, CourseContent, Enrollment


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context["enrolled"] = Enrollment.objects.filter(
                course=self.get_object(), user=self.request.user
            ).exists()
        except:
            context["enrolled"] = False
        context["course_content"] = CourseContent.objects.filter(
            course=self.get_object()
        )
        return context


class CourseContentView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=self.kwargs.get("course_slug"))
        enrollment = Enrollment.objects.filter(
            user=request.user, course=course
        ).exists()
        payment_exists = Payment.objects.filter(
            user=request.user,
            user_course__course=course,
            status="complete",
        ).exists()
        if enrollment and payment_exists:
            course_content = CourseContent.objects.filter(course=course)

            content1 = course_content.first()
            context = {
                "course": course,
                "course_content": course_content,
                "content1": content1,
            }
            return render(request, "courses/course_content.html", context)
        else:
            return render(request, "courses/course_not_enrolled.html", context)
