from django.shortcuts import render
from django.http import JsonResponse, HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer
from .models import DayResolution, Day
# Create your views here.

# def solve_day(request, day_solve_function, day):
#     try: 
#         if request.method == 'POST' and request.body:             
#             data = request.body.decode('utf-8')    
#             try:
#                 resolution = DayResolution.objects.get(input=data)
#                 if resolution:
#                     #get resolution.asnwer_part_one and resolution.answer_part_two
#                     pass
#                 else:
#                     result = day_solve_function(data)
#                     #create resolution, with input = data, day = day(foreign key), answer_part_one = result[1], answer_part_two = result[2]
#             except DayResolution.DoesNotExist:
#                   return JsonResponse({'error': 'No record found for the given date'}, status=404)

#         else:
#             result = day_solve_function()
#         return JsonResponse(result)
#     except Exception as e:
#         return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status = 400)

def create_days(request):
    if not Day.objects.exists() and request.method == "GET":
        for i in range(1, 26):
            Day.objects.create(
                number = i
            )
        return JsonResponse({'Success': 'Days database succesfully filled'})
    else:
        return JsonResponse({"error": "Wrong request method or days already exist."})
@csrf_exempt
def solve_day(request, day_solve_function, day):
    try:
        if request.method == 'POST' and request.body:
            data = request.body.decode('utf-8')
            try:
                resolution = DayResolution.objects.get(input=data)
                result = {
                    1: resolution.answer_part_one,
                    2: resolution.answer_part_two
                }
            except DayResolution.DoesNotExist:
                result = day_solve_function(data)
                # Create a new DayResolution object
                DayResolution.objects.create(
                    input=data,
                    day=Day.objects.get(number=day),
                    answer_part_one=result[1],
                    answer_part_two=result[2]
                )

        else:
            result = day_solve_function()

        return JsonResponse(result)
    except IndexError:
        return JsonResponse({'error': 'Index out of range. Make sure not to leave empty spaces at the end of the input'})
    except Exception as e:
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=400)

@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)