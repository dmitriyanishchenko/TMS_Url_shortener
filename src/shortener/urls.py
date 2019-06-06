from django.urls import path
from .views import (
    make,
    home,
)
urlpatterns = [
    path('', make, name='make'),
    path('<str:token>', home, name='Home'),


]

