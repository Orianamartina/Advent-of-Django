from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt    
from .forms.submit_answer import SubmissionForm
from django.utils.html import escape
from .models import DayResolution, Day,Language
from adventapi.models import CustomUser
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
                    resolution = DayResolution.objects.get(input=clean_form["input"].encode('utf-8'), user=user_id,day =clean_form["day"])
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
                            language = Language.objects.get(name=clean_form["language"]),
                            code = escape(clean_form["code"])   ,
                            user = CustomUser.objects.get(id=user_id),
                            description = clean_form['description'],
                        
                        )
                return JsonResponse({"Success":"Day resolution succesfully submited"})
            return JsonResponse({"error": "invalid form"})
        
    except IndexError:
        return JsonResponse({'error': 'Index out of range. Make sure not to leave empty spaces at the end of the input'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=400)


def filter_by_language(request, language):
    filtered_days = DayResolution.objects.filter(language = language)

    return render(request, 'filtered_home.html', {"days": filtered_days})