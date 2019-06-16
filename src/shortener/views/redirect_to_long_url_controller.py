from django.http import HttpResponse
from django.shortcuts import (
     redirect,
     get_object_or_404,
)
from shortener.functions import base_62_decode
from shortener.models import ShortUrls

HOST ='http://127.0.0.1:8000'


def redirect_to_long_url(request, link_id):
    """
    Принимает сокращенный URL, декодирует, и перенаправляет по длинному URL, считая клики

    """
    if request.method == 'GET':
        id = base_62_decode(link_id)
        url = get_object_or_404(ShortUrls, id=id)
        url.counter += 1
        url.save()
        return redirect(url.long_url)
    return HttpResponse('INVALID REQUEST')











