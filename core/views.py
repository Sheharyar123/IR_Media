from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from projects.models import Project

from .forms import ContactForm
from .utils import send_contact_email


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm
        projects = Project.objects.filter(is_active=True)
        context = {"form": form, "projects": projects}
        return render(request, "core/index.html", context)

    def post(self, request, *args, **kwargs):
        if request.headers.get("x-requested-with") == "XMLHttpRequest":
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            phone_no = request.POST.get("phone_no")
            email = request.POST.get("email")
            subject = request.POST.get("subject")
            project_details = request.POST.get("project_details")
            form = ContactForm(request.POST)
            if form.is_valid():
                context = {
                    "first_name": first_name,
                    "last_name": last_name,
                    "phone_no": phone_no,
                    "email": email,
                    "subject": subject,
                    "project_details": project_details,
                }
                send_contact_email("core/emails/send_contact_email.html", context)
                return JsonResponse({"status": "success"})
            else:
                return render(request, "core/index.html", {"form": form})
        else:
            return JsonResponse({"status": "failed"})
