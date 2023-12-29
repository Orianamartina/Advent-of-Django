from django.shortcuts import render
from django.http import JsonResponse, HttpResponse 
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from .serializers import UserSerializer
import json
from .models import DayResolution, Day
# Create your views here.
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
def solve_day(request, user_id, day_solve_function, day):
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
                    answer_part_two=result[2],
                    user = User.objects.get(id=user_id)
                )

        else:
            result = day_solve_function()

        return JsonResponse(result)
    except IndexError:
        return JsonResponse({'error': 'Index out of range. Make sure not to leave empty spaces at the end of the input'})
    except Exception as e:
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=400)

def get_user_days(user_id=1):
    try:
        resolutions = DayResolution.objects.filter(user = user_id)
        data = list(resolutions.values())
        return data
    except Exception as e:
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=400)




def home(request, user_id=1):
    user_info = get_user_days(user_id)

    return render(request, 'home.html', {'user': user_id, 'user_info': user_info})

@csrf_exempt
@api_view(['POST'])
def create_user(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = request.data["username"])
            user.set_password = request.data["password"]
            user.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
