from django.shortcuts import render, HttpResponse
import requests
from django.contrib.auth.models import User
from .forms import LoginForm


# Create your views here.


def index(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            req = requests.post("http://127.0.0.1:8000/api/auth/login/",
                                json={"username": cd['username'], "password": cd['password']})
            if req.status_code == 200:
                print("GOOD JOB")
                request.session["token"] = req.json()['access']
                print(request.session["token"])
            else:
                print("NOT GOOD")
    else:
        form = LoginForm()
    # token = req.json()['access']
    # print(token)
    # request.session["token"] = token
    # print(request.session["token"])
    # m = User.objects.get(username='admin')
    # if m.check_password('admin'):
    # print(request.user)
    # else:
    #     return HttpResponse("Your username and password didn't match.")
    return render(request, 'login.html', {"form": form})


def tournaments(request):
    req = requests.get(f"http://127.0.0.1:8000/api/tournaments/",
                       headers={"Authorization": f"Bearer {request.session['token']}"})
    print(request.session['token'])
    print(req.status_code)
    print(req.json())
    return HttpResponse('ELO ELO')
