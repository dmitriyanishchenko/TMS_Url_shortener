from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
)
from .models import ShortUrls
from .forms import UrlForm
from .shortner import shortner

HOST ='http://127.0.0.1:8000/'


def url_form_creator(request):
    """


    """
    urls_data = ShortUrls.objects.all()
    if request.method == 'GET':
        context = {'form': UrlForm(), 'urls_data': urls_data, 'HOST': HOST}
        return render(request, 'home.html', context)



# Create your views here.
