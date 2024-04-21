from django.core.management import BaseCommand

import csv

from dataentry.models import Student


# Proposed command - python manage.py importdata file_path
class Command(BaseCommand):
    help = 'Import data from CSV file'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        
    def handle(self, *args, **kwargs):
        # logic
        file_path = kwargs['file_path']
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)      # return DictReader object -> dict
            # reader2 = csv.reader(file)       # return reader object -> list
            for record in reader:
                Student.objects.create(**record)
        
        self.stdout.write(self.style.SUCCESS('Data is successfully imported.'))