from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, View
from .models import Course, Enrollment


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


class CourseContentView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        course = get_object_or_404(Course, slug=self.kwargs.get("course_slug"))
        enrollment = Enrollment.objects.filter(
            user=request.user, course=course
        ).exists()
        if enrollment:
            context = {"course": course}
            return render(request, "courses/course_content.html", context)
        else:
            return render(request, "courses/course_not_enrolled.html")
