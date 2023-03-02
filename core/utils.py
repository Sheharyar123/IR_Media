from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


def send_contact_email(mail_template, context):
    from_email = context.get("email")
    to_email = settings.EMAIL_HOST_USER
    mail_subject = "User Email From IR Media Website"
    message = render_to_string(mail_template, context)
    mail = EmailMessage(mail_subject, message, from_email, to=[to_email])
    mail.content_subtype = "html"
    mail.send()
