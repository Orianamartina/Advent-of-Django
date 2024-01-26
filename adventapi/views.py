from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse, HttpResponse 
from django.views.decorators.csrf import csrf_exempt    
from django.contrib.auth.decorators import login_required
from adventapi.forms.customCreateUser import CustomCreateUserForm
from django.contrib.auth import login, authenticate
from advent_days.forms.submit_answer import SubmissionForm
from .models import Comment, CustomUser, Like
from advent_days.models import DayResolution, Language
# Create your views here.

def delete_day(request, day):
    if request.method == "POST":
        try:
            user = request.user.id
            res = DayResolution.objects.get(user=user, day= day)
            res.delete()
            return JsonResponse({"Success": "Resolution succesfully deleted"})
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=400)


def get_user_days(request, user_id):
    if request.method == "GET":
        try:
            resolutions = DayResolution.objects.filter(user = user_id)
            data = list(resolutions.values())
            return JsonResponse({'data': data})
        except Exception as e:
            return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=400)


@login_required
def home(request):
    resolutions = DayResolution.objects.order_by('-id')[:10]
    user_id = request.user.id
    user = CustomUser.objects.get(id = user_id)
    likes = []
    languages = Language.objects.all()
    for res in resolutions:
        l = Like.objects.filter(user = user, post = res)
        if l:
            for i in l:
                likes.append(i.post_id)
    return render(request, 'home.html', {'user_id': user_id, 'recent': resolutions, "likes": likes, "languages": languages})



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
    res = DayResolution.objects.filter(user = user)
    return render(request, 'user/logged_in_profile.html', {'user': user, "r": res})

def resolution_code(request, resolution_id):
    res = get_object_or_404(DayResolution, id=resolution_id)
    comments = Comment.objects.filter(resolution = resolution_id)
    return render(request, 'code.html', {'res': res, 'replies': comments, 'id': resolution_id,})

def save_comment(request, resolution_id):
    comment_text = request.POST.get('comment')
    #comment_text = json.loads(request.data)
    user = CustomUser.objects.get(id=request.user.id)
    resolution = DayResolution.objects.get(id=resolution_id)

    # Create a new comment
    Comment.objects.create(
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

def like_post(request, post_id):
    if request.method == "POST":
        try:
            post = DayResolution.objects.get(id =post_id)
            post.likes += 1
            post.save()
            Like.objects.create(
                user = request.user,
                post = post
            )
            return JsonResponse({"success": "Post liked"})

        except Exception as e:
            return JsonResponse({"error: ": e})
        
def unlike_post(request, post_id):
    if request.method == "POST":
        try:
            post = DayResolution.objects.get(id =post_id)
            post.likes -= 1
            post.save()
            Like.objects.get(post = post, user = request.user).delete()
            return JsonResponse({"success": "Post unliked"})

        except Exception as e:
            return JsonResponse({"error: ": e})
        