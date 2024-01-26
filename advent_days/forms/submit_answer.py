from django import forms
from advent_days.models import Language
class SubmissionForm(forms.Form):
    days_choices = [ (i,i) for i in range(1,26)]
    language_choices = [(language.name, language.name) for language in Language.objects.all()]    
    language = forms.ChoiceField(choices=language_choices,widget=forms.Select(attrs={'class': 'custom-select'}))
    day = forms.ChoiceField(choices=days_choices,widget=forms.Select(attrs={'class': 'custom-select'}))
    input = forms.CharField(widget=forms.Textarea(attrs={'class':'input-input'}))
    code = forms.CharField(widget=forms.Textarea(attrs={'class':'input-input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'input-input'}))
    link_to_repo = forms.CharField()
    answer_part_one = forms.Textarea()
    answer_part_two = forms.Textarea()