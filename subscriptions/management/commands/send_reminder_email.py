import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.core.management.base import BaseCommand, CommandError

from subscriptions.models import Subscription

class Command(BaseCommand):
    help = 'Sends reminders to subscribers'

    def handle(self, *args, **options):
        try:
            print(f"HOST_USER: {settings.EMAIL_HOST_USER}")
            print(f"HOST: {settings.EMAIL_HOST}")

            subscriptions = Subscription.objects.all()
            today = datetime.date.today()
            for sub in subscriptions:
                #self.stdout.write(self.style.SUCCESS(f"{today} {sub.subscription_name} {sub.reminder_date}"))
                print(f"sub.subscription_name = {sub.subscription_name}")
                if sub.reminder_date == today and sub.active == True:
                    self.stdout.write(self.style.SUCCESS(f"Reminder: {sub.subscription_name}"))
                    # send mail 
                    subject = 'Reminder from Subscription Manager'
                    # user_email = User.objects.get(username=sub.subscriber).email
                    user_email = sub.reminder_email
                    message = f"Hi {sub.subscriber}, here is your reminder for {sub.subscription_name}.\r\n\r\n{sub.reminder_notes}\r\n\r\nThe Subscription Manager Team"
                    #message = f'{sub.reminder_notes}'
                    email_from = settings.EMAIL_HOST_USER
                    #print(settings.EMAIL_HOST_USER)
                    #user = User.objects.get(id=2)
                    #user_email = User.objects.get(username=2).user.email
                    if user_email and len(user_email) > 0:
                        print(user_email)
                        recipient_list = [user_email]
                        send_mail( subject, message, email_from, recipient_list )
                        self.stdout.write(self.style.SUCCESS(f"Mail sent to {user_email} for {sub.subscription_name}"))
                    else:
                        self.stdout.write(self.style.ERROR(f"No email address found for {sub.subscriber}"))
                else:
                    self.stdout.write(self.style.SUCCESS(f"No reminder for {sub.subscription_name}"))

        except FieldDoesNotExist:
            self.stdout.write(self.style.ERROR('Field "title" does not exist.'))
            return

        self.stdout.write(self.style.SUCCESS('Successfully iterated all subscriptions.'))
        return