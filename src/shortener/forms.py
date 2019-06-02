from django import forms


class UrlForm(forms.Form):
    original_url = forms.CharField(max_length=255)
    short_url = forms.CharField(max_length=255)
    #todo
