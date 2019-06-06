from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
)
from .models import Short_urls
from .forms import UrlForm
from .shortner import shortner

HOST ='http://127.0.0.1:8000/'


def make(request):
    """
    Функция вызывает форму для ввода длинного URL

    """
    form = UrlForm(request.POST)
    a = ''
    if request.method == "POST":
        if form.is_valid():
            new_url = form.save(commit=False)
            a = shortner().issue_token()

            new_url.save()
        else:
            form = UrlForm()
            a = "Invalid URL"
    return render(request, 'home.html', {'form': form, 'a': a})



def home(request, token):
    long_url = Short_urls.objects.filter(short_url=token)[0]
    return redirect(long_url.long_url)

# Create your views here.
