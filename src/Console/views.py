from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.http import StreamingHttpResponse
import os
from command import CommandRun

import command

# Create your views here.

@require_POST
def run_command(request):
    cmd = request.POST['command']
    result = command.run_command(cmd, (os.path.join(os.path.dirname(__file__), '../WebConsole'))) 
    return JsonResponse(result)

def download_result_file(request, file_name):
    return StreamingHttpResponse(CommandRun.get_result_file(file_name), content_type='plain/text')
