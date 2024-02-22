from django.urls import path
from . import views

app_name = 'torg_app'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login_view'),
]
