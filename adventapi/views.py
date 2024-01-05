from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse 
from django.views.decorators.csrf import csrf_exempt    
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms.submit_answer import SubmissionForm
import json
from .models import DayResolution, Day, RecentResolutions
from .days.solve import solve
# Create your views here.
@csrf_exempt
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

def solve_day(request, user_id):
    try:
        if request.method == 'POST' and request.body:
            form = SubmissionForm(request.POST)
            if form.is_valid():
                clean_form = form.cleaned_data
                try:
                    resolution = DayResolution.objects.get(input=clean_form["input"], user=user_id,day =clean_form["day"])
                    result = {
                        1: resolution.answer_part_one,
                        2: resolution.answer_part_two
                    }
               

                except DayResolution.DoesNotExist:
                        result = solve(clean_form["day"],clean_form["input"])       
                        # Create a new DayResolution object
                        day_resolution = DayResolution.objects.create(
                            input=clean_form["input"],
                            day=Day.objects.get(number=clean_form["day"]),
                            answer_part_one=result[1],
                            answer_part_two=result[2],
                            language = clean_form["language"],
                            code = clean_form["code"],
                            user = User.objects.get(id=user_id)
                        )
                        RecentResolutions.objects.create(
                            user = User.objects.get(id=user_id),
                            resolution = DayResolution.objects.get(user=user_id, day=clean_form["day"])
                        )
                return JsonResponse({"Success":"Day resolution succesfully submited"})
            return JsonResponse({"error": "invalid form"})
        
    except IndexError:
        return JsonResponse({'error': 'Index out of range. Make sure not to leave empty spaces at the end of the input'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=400)

@csrf_exempt

def get_user_days(request, user_id):
    if request.method == "GET":
        try:
            resolutions = DayResolution.objects.filter(user = user_id)
            data = list(resolutions.values())
            return JsonResponse({'data': data})
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=400)
    

def home(request):
    recent = RecentResolutions.objects.select_related('resolution')
    user_id = request.user.id
    return render(request, 'home.html', {'user_id': user_id, 'recent': recent})

def submit_input(request):
    days = [i for i in range(1,26)]
    user = request.user
    form = SubmissionForm()
    return render(request, 'submit_input.html', {'days': days, 'id': user.id, 'form':form})

def profile(request):
    user = request.user    
    resolutions = DayResolution.objects.filter(user = user.id)
    data = list(resolutions.values())
    return render(request, 'profile/profile.html', {'user': user, 'resolutions':data})

@csrf_exempt

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})