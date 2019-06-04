from django import forms


class UrlForm(forms.Form):
    full_url = forms.CharField(max_length=150)
    short_url = forms.CharField(max_length=150)
    date_add = forms.DateTimeField()
    counter_click = forms.IntegerField()
