from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views.decorators.http import require_POST
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@require_POST
def solve_day(request, day_solve_function):
    try: 
        if request.body:            
            data = request.body.decode('utf-8')
            result = day_solve_function(data)
        else:
            result = day_solve_function()
        return JsonResponse(result)
    except Exception as e:
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status = 400)
