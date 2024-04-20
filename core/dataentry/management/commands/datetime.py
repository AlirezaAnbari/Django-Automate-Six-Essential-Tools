from django.core.management.base import BaseCommand

from django.utils import timezone
from datetime import datetime, timedelta


OSTAN_LIST = [
    "Alborz",
    "Ardabil",
    "Azerbaijan East",
    "Azerbaijan West",
    "Bushehr",
    "Chaharmahal and Bakhtiari",
    "East Azerbaijan",
    "Esfahan",
    "Fars",
    "Gilan",
    "Golestan",
    "Hormozgan",
    "Ilam",
    "Isfahan",
    "Kerman",
    "Kermanshah",
    "Khuzestan",
    "Kohgiluyeh and Boyer-Ahmad",
    "Kurdistan",
    "Lorestan",
    "Markazi",
    "Mazandaran",
    "Qom",
    "Semnan",
    "Sistan and Baluchestan",
    "South Khorasan",
    "Tehran",
    "West Azerbaijan",
    "Yazd",
    "Zanjan",
]


class Command(BaseCommand):
    help = '''
            Displays current time for Iran.
            Usage: python manage.py greeting Iran
            '''

    def add_arguments(self, parser):
        parser.add_argument('ostan', type=str, help='Ostan name')

    def handle(self, *args, **kwargs):
        ostan = kwargs['ostan'].lower()

        # Check if the country is Iran or any city within Iran
        if ostan == 'iran' or ostan in [ostan.lower() for ostan in OSTAN_LIST]:
            current_utc_time = timezone.now()
            new_time = current_utc_time + timedelta(hours=3, minutes=30)
            current_time = new_time.strftime("%Y-%m-%d %H:%M:%S")
            self.stdout.write(f"It's now {current_time} - {ostan}")
        else:
            self.stderr.write(f"We only support showing time for Iran or its ostans.")