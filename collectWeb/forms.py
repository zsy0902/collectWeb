from django import forms

# forms.py


class AudioForm(forms.Form):
    id = forms.CharField(max_length=55)
    testDate = forms.CharField(max_length=20)
    audio = forms.FileField()

