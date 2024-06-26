from django.urls import path
from . import views

app_name = 'players'

urlpatterns = [
    path('', views.PlayersListView.as_view(), name='players_list'),
    path('<int:pk>/', views.PlayerDetailsView.as_view(), name='player_details')
]
