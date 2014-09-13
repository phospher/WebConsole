from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
import os

from command.CommandParse import parse_input
from command.Configurations import CommandConfigurationManager

# Create your views here.

@require_POST
def run_command(request):
    cmd = request.POST['command']
    configs = CommandConfigurationManager(os.path.join(os.path.dirname(__file__), '../WebConsole'))._read_config_from_file()
    return JsonResponse({'type':'CONSOLE', 'result':'cmd:{0}--callableObject:{1}'.format(configs[0].command, configs[0].callable_object)})
