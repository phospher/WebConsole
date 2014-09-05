from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.http import JsonResponse

# Create your views here.

@require_POST
def run_command(request):
    cmd = request.POST['command']
    return JsonResponse({'type':'CONSOLE', 'result':cmd})
