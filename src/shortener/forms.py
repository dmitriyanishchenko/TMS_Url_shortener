from django import forms


class UrlForm(forms.Form):
    original_url = forms.CharField(max_length=150)
    short_url = forms.CharField(max_length=150)
    add = forms.DateTimeField(null=False)
    counter_click = forms.PositiveSmallIntegerField()
