from django.apps import apps
from django.apps import apps as django_apps


def get_all_custom_models():
    default_models = [
        'ContentType', 'Session', 'LogEntry', 'Group', 'Permission',
    ]
    
    custom_models = []
    for model in apps.get_models():
        if not model.__module__.startswith('django.contrib'): # exclude default django models
            custom_models.append(model.__name__)
            
    return custom_models