from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import RSVP

@receiver(post_save, sender=RSVP)
def send_confirmation_email(sender, instance, created, **kwargs):
    if created:  
        subject = 'Event Registration Confirmation'
        message = f'''
        Hello {instance.user.username},

        You have successfully registered for the event: {instance.event.name}.

        Event Details:
        - Date: {instance.event.date}
        - Time: {instance.event.time}
        - Location: {instance.event.location}

        Thank you for registering!
        '''
        from_email = settings.EMAIL_HOST_USER
        to_email = [instance.user.email]

        send_mail(subject, message, from_email, to_email, fail_silently=False)
