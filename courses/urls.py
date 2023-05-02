from django.urls import path
from .views import CourseListView, CourseDetailView, CourseContentView

app_name = "courses"

urlpatterns = [
    path("", CourseListView.as_view(), name="course_list"),
    path("<slug:course_slug>/", CourseDetailView.as_view(), name="course_detail"),
    path(
        "<slug:course_slug>/content", CourseContentView.as_view(), name="course_content"
    ),
]
