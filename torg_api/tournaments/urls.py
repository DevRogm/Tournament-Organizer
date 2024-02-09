from django.urls import path
from . import views

app_name = 'tournaments'

urlpatterns = [
    path('tournaments/', views.TournamentListView.as_view(), name='tournaments_list')
]