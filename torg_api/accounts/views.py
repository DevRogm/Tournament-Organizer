from .serializers import UserSerializer, MyTokenObtainPairSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

@api_view(['GET'])
def get_user_profile(request):
    user = request.user
    serializer = UserSerializer(user, many=False)
    return Response(serializer.data)
