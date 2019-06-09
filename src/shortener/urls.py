from django.urls import path

from .views import (
    url_form_creator,
    redirect_to_long_url

)
urlpatterns = [
    path('', url_form_creator),
    path('<str:link_id>/', redirect_to_long_url),



]

