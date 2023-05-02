import stripe
from decimal import Decimal
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.conf import settings
from django.views.generic import View
from django.contrib.auth.mixins import LoginRequiredMixin
from courses.models import Course

stripe.api_key = settings.STRIPE_SECRET_KEY
stripe.api_version = settings.STRIPE_API_VERSION

# Update the PaymentView class


class PaymentView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        try:
            success_url = request.build_absolute_uri(
                reverse("payments:payment_completed")
            )
            cancel_url = request.build_absolute_uri(
                reverse("payments:payment_canceled")
            )
            course_id = kwargs.get("course_id")
            course = get_object_or_404(Course, id=course_id, is_active=True)
            session_data = {
                "mode": "payment",
                "client_reference_id": course_id,
                "success_url": success_url,
                "cancel_url": cancel_url,
                "line_items": [],
                # "customer_email": subscription.email,
            }

            session_data["line_items"].append(
                {
                    "price_data": {
                        "unit_amount": int(course.price * Decimal("100")),
                        "currency": "usd",
                        "product_data": {"name": course.title},
                    },
                    "quantity": 1,
                }
            )

            session = stripe.checkout.Session.create(**session_data)
            return redirect(session.url, code=303)

        except:
            return redirect("courses:course_list")


class PaymentCompletedView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        return render(request, "payments/payment_completed.html")


class PaymentCanceledView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "payments/payment_canceled.html")
