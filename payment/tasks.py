from django.core.mail import send_mail
from celery import shared_task


@shared_task
def send_transaction_notification_email(recipient_email, amount):
    subject = 'Transaction Notification'
    message = f'Your account has been credited with ${amount}.'
    sender_email = 'bektemirsatybaldiev@gmail.com'
    recipient_list = [recipient_email]
    return send_mail(subject, message, sender_email, recipient_list)
