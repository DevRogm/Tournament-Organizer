from django.urls import path
from . import views

app_name = 'torg_app'

urlpatterns = [
    path('', views.index, name='index'),
    path('tournaments/', views.tournaments, name='tournaments')
]
