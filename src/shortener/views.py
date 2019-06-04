from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
)
from shortener.models import ShortUrl
from shortener.forms import UrlForm


def added_url(request):
    """
    Функция вызывает форму для ввода длинного урла
    :param request:
    :return:
    """
    if request.method == 'GET':
        form = UrlForm()
        context = {'form': form}
        return render(request, 'home.html', context)






# Create your views here.
