from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import Group
User = get_user_model()
@receiver(post_save,sender=User)
def send_activation_email(sender, instance, created, **kwargs):
    if created:
        token = default_token_generator.make_token(instance)
        activation_link=f"{settings.FRONTEND_URL}/users/activate/{instance.id}/{token}/"
        subject = 'Activate Your Account'
        message = f"Click the link to activate your account: <a href='{activation_link}'>Activate</a>"
        recipient_list = [instance.email]

        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        except Exception as e:
            print(f"Failed to send email to {instance.email}: {str(e)}")
@receiver(post_save,sender=User)
def assign_role(sender, instance, created, **kwargs):
    if created:
        user_group , created = Group.objects.get_or_create(name='User')
        instance.groups.add(user_group)
        instance.save()