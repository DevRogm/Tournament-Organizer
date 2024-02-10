from django.urls import path
from . import views

app_name = 'games'

urlpatterns = [
    path('', views.GameListView.as_view(), name='games_list')
]
