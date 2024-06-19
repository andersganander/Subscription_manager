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
                self.stdout.write(self.style.SUCCESS(f"sub.subscription_name: {sub.subscription_name}"))
                if sub.reminder_date == today and sub.active == True:
                    self.stdout.write(self.style.SUCCESS(f"Reminder: {sub.subscription_name}"))
                    # compose mail 
                    subject = 'Reminder from Subscription Manager'
                    user_email = sub.reminder_email
                    message = f"Hi {sub.subscriber}, here is your reminder for {sub.subscription_name}.\r\n\r\n{sub.reminder_notes}\r\n\r\nThe Subscription Manager Team"
                    email_from = settings.EMAIL_HOST_USER
                    if user_email and len(user_email) > 0:
                        print(user_email)
                        recipient_list = [user_email]
                        # send mail
                        send_mail( subject, message, email_from, recipient_list )
                        self.stdout.write(self.style.SUCCESS(f"Mail sent to {user_email} for {sub.subscription_name}"))
                    else:
                        self.stdout.write(self.style.ERROR(f"No email address found for {sub.subscriber}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"No reminder for {sub.subscription_name}"))

        except FieldDoesNotExist:
            self.stdout.write(self.style.ERROR('Field does not exist.'))
            return

        self.stdout.write(self.style.SUCCESS('Successfully iterated all subscriptions.'))
        return