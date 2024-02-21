from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('user/', views.get_user_profile, name='user'),
    path('register/', views.register_user, name='register'),
]
