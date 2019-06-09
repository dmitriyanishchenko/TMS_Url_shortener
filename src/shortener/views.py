from django.http import HttpResponse
from django.shortcuts import (
    render,
    redirect,
    get_object_or_404
)

from shortener.functions import base_62_decode
from shortener.functions import base_62_encode
from .models import ShortUrls
from .forms import UrlForm

HOST ='http://127.0.0.1:8000'


def url_form_creator(request):
    """
    Направляет на домашнюю страницу и обрабатывает форму

    """
    urls_data = ShortUrls.objects.all()
    if request.method == 'GET':
        context = {'form': UrlForm(), 'urls_data': urls_data, 'HOST': HOST}
        return render(request, 'home.html', context)
    elif request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data.get('long_url')
            if ShortUrls.objects.filter(long_url=long_url).exists():
                current_url = ShortUrls.objects.get(long_url=long_url)
                context = {'short_url': f'{HOST}/{current_url.short_url}', 'HOST': HOST}
                return render(request, 'edit_url.html', context)
            else:
                current_url = ShortUrls(long_url=long_url)
                current_url.save()
                current_url.short_url = base_62_encode(current_url.id)
                current_url.save()
                context = {'short_url': f'{HOST}/{current_url.short_url}', 'HOST': HOST}
                return render(request, 'edit_url.html', context)
        else:
            errors = form.errors
            return HttpResponse(errors)
    else:
        return HttpResponse('INVALID REQUEST')


def redirect_to_long_url(request, link_id):
    if request.method == 'GET':
        id = base_62_decode(link_id)
        url = get_object_or_404(ShortUrls, id=id)
        url.counter += 1
        url.save()
        return redirect(url.long_url)
    return HttpResponse('INVALID REQUEST')













# Create your views here.
