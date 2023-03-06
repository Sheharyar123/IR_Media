from django.urls import path
from .views import ProjectDetailView

app_name = "projects"

urlpatterns = [
    path("project/<slug>/", ProjectDetailView.as_view(), name="project_detail"),
]
