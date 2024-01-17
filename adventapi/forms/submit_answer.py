from django import forms

class SubmissionForm(forms.Form):
    days_choices = [ (i,i) for i in range(1,26)]
    language = forms.CharField(widget=forms.TextInput(attrs={'class':'input-language'}))
    day = forms.ChoiceField(choices=days_choices,widget=forms.Select(attrs={'class': 'custom-select'}))
    input = forms.CharField(widget=forms.Textarea(attrs={'class':'input-input'}))
    code = forms.CharField(widget=forms.Textarea(attrs={'class':'input-input'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'input-input'}))
