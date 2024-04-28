from django.core.management import BaseCommand, CommandError
from django.apps import apps
from django.db.utils import DataError

import csv


# Proposed command : python manage.py importdata file_path model_name
class Command(BaseCommand):
    help = 'Import data from CSV file'
    
    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Name of the model')
        
    def handle(self, *args, **kwargs):
        # logic
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()
        
        # Search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            try:
                model = apps.get_model(app_config.label, model_name)
                break # stop searching once the model is found
            except LookupError:
                continue # model not found in this app, continue searching in next app
            
        if not model:
            raise CommandError(f'Model {model_name} not found in any apps!')
            
        # Get all the fields name of the model that we found
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)      # return DictReader object -> dict
            csv_header = reader.fieldnames
            
            # Compare CSV header with model's field names
            if csv_header != model_fields:
                raise DataError(f'CSV file does not match with the {model_name} field names.')
            
            for record in reader:
                model.objects.create(**record)
        
        self.stdout.write(self.style.SUCCESS('Data is successfully imported.'))