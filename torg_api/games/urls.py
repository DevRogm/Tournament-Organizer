from django.urls import path
from . import views
app_name = 'games'

urlpatterns = [
    path('games/', views.GameListView.as_view(), name='games_list')
]