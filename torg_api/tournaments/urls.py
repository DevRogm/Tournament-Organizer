from django.urls import path
from . import views

app_name = 'tournaments'

urlpatterns = [
    path('', views.TournamentListView.as_view(), name='tournaments_list'),
    path('<pk>/', views.TournamentDetailView.as_view(), name='tournament_details'),
]
