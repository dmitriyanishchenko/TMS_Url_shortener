from django.urls import path
from .views import (
    url_form_creator,

)
urlpatterns = [
    path('', url_form_creator),



]

