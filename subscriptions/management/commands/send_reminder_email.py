import datetime
from django.core.management.base import BaseCommand, CommandError
from subscriptions.models import Subscription

class Command(BaseCommand):
    help = 'Sends reminders to subscribers'

    def handle(self, *args, **options):
        try:
            subscriptions = Subscription.objects.all()
            today = datetime.date.today()
            for sub in subscriptions:
                #self.stdout.write(self.style.SUCCESS(f"{today} {sub.subscription_name} {sub.reminder_date}"))

                if sub.reminder_date == today and sub.active == True:
                    self.stdout.write(self.style.SUCCESS(f"Reminder: {sub.subscription_name}"))
        except FieldDoesNotExist:
            self.stdout.write(self.style.ERROR('Field "title" does not exist.'))
            return

        self.stdout.write(self.style.SUCCESS('Successfully iterated all subscriptions.'))
        return