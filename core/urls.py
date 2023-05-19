from django.urls import path
from .views import (
    HomePageView,
    TermsAndConditionsView,
    RefundPolicyView,
    PrivacyPolicyView,
)

app_name = "core"

urlpatterns = [
    path("", HomePageView.as_view(), name="index"),
    path("terms_and_conditions/", TermsAndConditionsView.as_view(), name="terms"),
    path("refund_policy/", RefundPolicyView.as_view(), name="refund"),
    path("privacy_policy/", PrivacyPolicyView.as_view(), name="privacy"),
]
