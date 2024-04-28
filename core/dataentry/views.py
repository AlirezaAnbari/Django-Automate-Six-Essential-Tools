from django.shortcuts import render, redirect
from django.conf import settings
from django.core.management import call_command
from django.contrib import messages

from .utils import get_all_custom_models
from uploads.models import Upload


def import_data(request):
    if request.method == 'POST':
        file_path = request.FILES['file_path']
        model_name = request.POST['model_name']
        
        # store this file inside the upload model
        upload = Upload.objects.create(file=file_path, model_name=model_name)
        
        # construct the full path
        relative_path = str(upload.file.url)
        base_url = str(settings.BASE_DIR)
        
        file_full_path = base_url + relative_path
        
        # trigger the importdata command to view
        try:
            call_command('importdata', file_full_path, model_name)
            messages.success(request, 'Data imported successfully.')
        except Exception as e:
            messages.error(request, str(e))
        
        return redirect('import_data')
    else:
        # Get all the custom models in each apps(utils.py)
        custom_models = get_all_custom_models()
        
        context = {
            'custom_models': custom_models,
        }
        
    return render(request, 'dataentry/import_data.html', context)