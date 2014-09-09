from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse

from command.CommandParse import parse_input

# Create your views here.

@require_POST
def run_command(request):
    cmd = request.POST['command']
    parse_result = parse_input(cmd)
    return JsonResponse({'type':'CONSOLE', 'result':'cmd:{0}--args:{1}--output_type:{2}--output_name:{3}'.format(parse_result.command, parse_result.args, parse_result.output_type, parse_result.output_name)})
