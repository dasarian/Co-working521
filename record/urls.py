
from django.urls import path
from . import views

urlpatterns = [
    path('', views.record_main_page, name='record_main_page'),
]