from django.core.mail import send_mail

from django.conf import settings


def send_email_to_user(email, code):
    send_mail(
        subject='Confirm Email',
        message=f'Sizning Shop project uchun TASDIQLASH codingiz {code}',
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email]
    )
