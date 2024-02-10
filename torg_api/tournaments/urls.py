from django.urls import path
from . import views

app_name = 'tournaments'

urlpatterns = [
    path('', views.TournamentListView.as_view(), name='tournaments_list'),
    path('<pk>/', views.TournamentDetailsView.as_view(), name='tournament_details'),
]
