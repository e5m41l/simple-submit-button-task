from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_view, name='submit_form'),
]
