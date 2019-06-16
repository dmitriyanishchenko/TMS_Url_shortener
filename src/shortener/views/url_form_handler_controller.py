from django.http import HttpResponse
from django.shortcuts import render
from shortener.functions import base_62_encode
from shortener.models import ShortUrls
from shortener.forms import UrlForm

HOST = 'http://127.0.0.1:8000'


def url_form_handler(request):
    """
    Направляет на домашнюю страницу и обрабатывает форму

    """
    urls_from_db = ShortUrls.objects.all()
    if request.method == 'GET':
        context = {'form': UrlForm(), 'urls_from_db': urls_from_db, 'HOST': HOST}
        return render(request, 'shortener/home.html', context)
    elif request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            long_url = form.cleaned_data.get('long_url')
            if ShortUrls.objects.filter(long_url=long_url).exists():
                current_url = ShortUrls.objects.get(long_url=long_url)
                context = {'short_url': f'{HOST}/{current_url.short_url}', 'HOST': HOST}
                return render(request, 'shortener/edit_url.html', context)
            else:
                current_url = ShortUrls(long_url=long_url)
                current_url.save()
                current_url.short_url = base_62_encode(current_url.id)
                current_url.save()
                context = {'short_url': f'{HOST}/{current_url.short_url}', 'HOST': HOST}
                return render(request, 'shortener/edit_url.html', context)
        else:
            errors = form.errors
            return HttpResponse(errors)
    else:
        return HttpResponse('INVALID REQUEST')
