# Add some data to the DataBase using custom command.

from typing import Any
from django.core.management import BaseCommand

from dataentry.models import Student


class Command(BaseCommand):
    help = 'Insert data into the DataBase'
    
    def handle(self, *args, **options):
        
        # Add 1 data
        # Student.objects.create(roll_no=1001,name='Alireza',age=27)
        
        # Add more data
        dataset = [
            {'roll_no': 1002, 'name': 'saman', 'age':21},
            {'roll_no': 1003, 'name': 'sadaf', 'age':25},
            {'roll_no': 1004, 'name': 'sina', 'age':30},
        ]
        
        for data in dataset:
            Student.objects.create(
                roll_no=data['roll_no'],
                name=data['name'],
                age=data['age'],
            )
        
        self.stdout.write(self.style.SUCCESS('Data inserted successfully.'))