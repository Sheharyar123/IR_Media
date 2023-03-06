from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from .models import Project


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/project_detail.html"
    context_object_name = "project"

    def get_object(self):
        queryset = get_object_or_404(
            Project, slug=self.kwargs.get("slug"), is_active=True
        )
        return queryset
