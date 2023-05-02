from django.urls import path
from .views import PaymentView, PaymentCompletedView, PaymentCanceledView

app_name = "payments"

urlpatterns = [
    path("<uuid:course_id>/", PaymentView.as_view(), name="check_payment"),
    path("completed/", PaymentCompletedView.as_view(), name="payment_completed"),
    path("canceled/", PaymentView.as_view(), name="payment_canceled"),
]
