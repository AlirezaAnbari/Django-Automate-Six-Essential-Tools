from django.apps import apps
from django.apps import apps as django_apps


def get_all_custom_models():
    # default_models = [
    #     'ContentType', 'Session', 'LogEntry', 'Group', 'Permission',
    # ]
    default_models = [model.__name__ for model in apps.get_models() if model.__module__.startswith('django.contrib')]
    exclude_models = ['Upload']
    exclude_models += default_models
    
    custom_models = []
    for model in apps.get_models():
        # if not model.__module__.startswith('django.contrib') and  not exclude_models: # exclude default django models and upload
        #     custom_models.append(model.__name__)
        if model.__name__ not in exclude_models:
            custom_models.append(model.__name__)
    return custom_models