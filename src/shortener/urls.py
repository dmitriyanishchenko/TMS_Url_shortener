from django.urls import path
from .views import (
    added_url
)
urlpatterns = [
    path('', added_url, name='added_url'),


]

