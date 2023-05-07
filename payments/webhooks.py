# import stripe
# from decimal import Decimal
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from courses.models import Enrollment, Course
# from .models import Payment

# User = get_user_model()


# @csrf_exempt
# def stripe_webhook(request):
#     payload = request.body
#     sig_header = request.META["HTTP_STRIPE_SIGNATURE"]
#     event = None
#     try:
#         event = stripe.Webhook.construct_event(
#             payload, sig_header, settings.STRIPE_WEBHOOK_SECRET
#         )
#     except ValueError as e:
#         # Invalid payload
#         return HttpResponse(status=400)
#     except stripe.error.SignatureVerificationError as e:
#         # Invalid signature
#         return HttpResponse(status=400)

#     if event.type == "checkout.session.completed":
#         session = event.data.object
#         if session.mode == "payment" and session.payment_status == "paid":
#             try:
#                 course = Course.objects.get(
#                     id=session.client_reference_id, is_active=True
#                 )
#                 user = User.objects.get(email=session.customer_email)
#                 enrollment = Enrollment.objects.create(user=user, course=course)
#                 Payment.objects.create(
#                     user=user,
#                     user_course=enrollment,
#                     stripe_payment_id=session.payment_intent,
#                     amount=Decimal(session.amount_total) / 100,
#                     status=session.status,
#                 )
#             except Enrollment.DoesNotExist:
#                 return HttpResponse(status=404)
#     return HttpResponse(status=200)
