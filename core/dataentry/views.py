from django.shortcuts import render

from .utils import get_all_custom_models


def import_data(request):
    if request.method == 'POST':
        return
    else:
        # Get all the custom models in each apps(utils.py)
        custom_models = get_all_custom_models()
        
        context = {
            'custom_models': custom_models,
        }
        
    return render(request, 'dataentry/import_data.html', context)