from django.urls import path

from . import views

app_name = 'cv'

urlpatterns = [
    path(r'maxxtor/', views.MaxxtorCvView.as_view(), name='maxxtor'),
    path(r'alexshow/', views.AlexshowCvView.as_view(), name='alexshow'),
    path(r'elenashow/', views.ElenashowCvView.as_view(), name='elenashow'),
]
