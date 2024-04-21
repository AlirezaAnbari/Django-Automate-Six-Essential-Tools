from django.core.management import BaseCommand

import csv
import datetime

from dataentry.models import Student


# Proposed command : python manage.py exportdata
class Command(BaseCommand):
    help = 'Export data'
        
    def handle(self, *args, **kwargs):
        # Fetch the data from the database
        students = Student.objects.all() 
        
        # Generate the timestamp of current date and time
        timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')
        
        # Define the CSV file name
        file_path = f'exported_student_data_{timestamp}.csv'
        
        # Open the CSV file and write the data
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            
            # CSV header
            writer.writerow(['Roll No', 'Name', 'Age'])
            
            # Write data rows
            for student in students:
                writer.writerow([student.roll_no, student.name, student.age])
                
        self.stdout.write(self.style.SUCCESS('Data exported successfully.'))