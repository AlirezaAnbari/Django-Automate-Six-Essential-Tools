# Add some data to the DataBase using custom command.

from typing import Any
from django.core.management import BaseCommand

from dataentry.models import Student


class Command(BaseCommand):
    help = 'Insert data into the DataBase'
    
    def handle(self, *args, **options):
        
        # Add 1 data
        # Student.objects.create(roll_no=1001,name='Alireza',age=27)
        
        # Add bunch of data
        dataset = [
            {'roll_no': 1008, 'name': 'marjan', 'age':21},
            {'roll_no': 1009, 'name': 'sama', 'age':25},
            {'roll_no': 1010, 'name': 'mansour', 'age':30},
        ]
        
        stdent_count = 0
        for data in dataset:
            roll_no = data['roll_no']
            existing_roll_no_record = Student.objects.filter(roll_no=roll_no).exists()
            
            if not existing_roll_no_record:
                Student.objects.create(
                    roll_no=data['roll_no'],
                    name=data['name'],
                    age=data['age'],
                )
                
                stdent_count += 1
            else:
                self.stdout.write(self.style.WARNING(f'Student with roll no {roll_no} already exist!'))
                
        self.stdout.write(self.style.SUCCESS(f'Data inserted successfully.\n{stdent_count} added.'))