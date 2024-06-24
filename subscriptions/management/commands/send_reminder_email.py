import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError

from subscriptions.models import Subscription

class Command(BaseCommand):
    help = 'Sends reminders to subscribers'

    def handle(self, *args, **options):
        """
        This function iterates over all subscriptions, checks if a reminder needs to be sent, 
        and sends the reminder email if necessary.

        Parameters:
        *args: Not used in this function.
        **options: Not used in this function.

        Returns:
        None
        """
        try:
            subscriptions = Subscription.objects.all()
            today = datetime.date.today()
            for sub in subscriptions:
                if sub.reminder_date == today and sub.active == True:
                    # compose mail 
                    subject = 'Reminder from Subscription Manager'
                    user_email = sub.reminder_email
                    message = f"Hi {sub.subscriber}, here is your reminder for {sub.subscription_name}.\r\n\r\n{sub.reminder_notes}\r\n\r\nThe Subscription Manager Team"
                    email_from = settings.EMAIL_HOST_USER
                    if user_email and len(user_email) > 0:
                        recipient_list = [user_email]
                        # send mail
                        send_mail( subject, message, email_from, recipient_list )
                    else:
                        pass
                else:
                    pass

        except FieldDoesNotExist:
            return
        return