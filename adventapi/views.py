from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse 
from django.views.decorators.csrf import csrf_exempt    
from adventapi.forms.customCreateUser import CustomCreateUserForm
from django.contrib.auth import login, authenticate
from .forms.submit_answer import SubmissionForm
from django.utils.html import escape
import json
from .models import DayResolution, Day, RecentResolutions, Reply, CustomUser
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
                            code = escape(clean_form["code"])   ,
                            user = CustomUser.objects.get(id=user_id),
                            description = clean_form['comment']
                        )
                        RecentResolutions.objects.create(
                            user = CustomUser.objects.get(id=user_id),
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
    resolutions = DayResolution.objects.order_by('-id')[:10]
    user_id = request.user.id
    return render(request, 'home.html', {'user_id': user_id, 'recent': resolutions})

def submit_input(request):
    days = [i for i in range(1,26)]
    user = request.user
    form = SubmissionForm()
    return render(request, 'submit_input.html', {'days': days, 'id': user.id, 'form':form})

@csrf_exempt

def signup(request):
    if request.method == 'POST':
        form = CustomCreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomCreateUserForm()
    return render(request, 'signup.html', {'form': form})

def user_profile(request, username):
    user = get_object_or_404(CustomUser, username=username)
    resolutions = DayResolution.objects.filter(user=user).order_by("id")
    return render(request, 'user_profile.html', {'user': user, 'resolutions': resolutions})

def my_profile(request):
    id = request.user.id
    user = CustomUser.objects.get(id=id)
    return render(request, 'user/logged_in_profile.html', {'user': user})

def resolution_code(request, resolution_id):
    res = get_object_or_404(DayResolution, id=resolution_id)
    comments = Reply.objects.filter(resolution = resolution_id)
    return render(request, 'code.html', {'res': res, 'replies': comments, 'id': resolution_id,})

def save_comment(request, resolution_id):
    #comment_text = request.POST.get('comment')
    comment_text = json.loads(request.data)
    user = CustomUser.objects.get(id=request.user.id)
    resolution = DayResolution.objects.get(id=resolution_id)

    # Create a new comment
    Reply.objects.create(
        user=user,
        resolution=resolution,
        text=comment_text
    )

    # Increment the comments_quantity of the resolution
    resolution.comments_quantity += 1
    resolution.save()

    return JsonResponse({"Success":"Comment succesfully submited"})
    

def upload_image(request):
    if request.method == "POST":
        try:
            id = request.user.id
            user = CustomUser.objects.get(id=id)
            image = request.POST.get('image_url')
            user.image = image
            user.save()
            return JsonResponse({"Success": "Image succesfully updated"})
        except:
            return JsonResponse({"Error": "An error ocurred"})

def update_image_template_view(request):
    return render(request, 'user/upload_image.html')