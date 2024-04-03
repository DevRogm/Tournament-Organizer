from django.contrib.auth.decorators import login_required
from django.shortcuts import render, HttpResponse, redirect, Http404
import requests
from django.contrib.auth.models import User
from .forms import LoginForm

# Create your views here.
URL_API = "http://127.0.0.1:8000/"


def headers(request):
    token = request.session.get("token")
    if token:
        header = {
            "Authorization": "Bearer " + token
        }
        return header
    else:
        return None


def is_auth(request):
    token = request.session.get("token")
    if token:
        return True
    else:
        return False


def dashboard(request):
    if not is_auth(request):
        return redirect('torg_app:login_view')
    url = "/api/tournaments/"
    ongoing_filter = "?tournament_status=ongoing"
    waiting_filter = "?tournament_status=waiting"
    complete_filter = "?tournament_status=complete"
    req_ongoing = requests.get(URL_API+url+ongoing_filter, headers=headers(request))
    req_waiting = requests.get(URL_API+url+complete_filter, headers=headers(request))
    req_complete = requests.get(URL_API+url+ongoing_filter, headers=headers(request))
    print(req.json())
    # ongoing_tour = len(Tournament.status_ongoing.filter(author=request.user))
    # completed_tour = len(Tournament.status_completed.filter(author=request.user))
    # waiting_tour = len(Tournament.status_waiting.filter(author=request.user))
    # print(ongoing_tour)
    # print(completed_tour)
    # print(waiting_tour)
    return render(request, 'torg_app/dashboard.html',
                  {'section': 'dashboard',
                   # 'ong_tour': ong_tour,
                   # 'fin_tour': fin_tour,
                   # 'pen_tour': pen_tour,
                   })


def login(request):
    url = "api/auth/login/"
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            req = requests.post(URL_API + url, json={"username": cd['username'], "password": cd['password']})
            if req.status_code == 200:
                request.session["token"] = req.json()['access']
            else:
                return HttpResponse("Wrong input data")
        if request.session.get("token"):
            return redirect('torg_app:dashboard')
    else:
        form = LoginForm()
    return render(request, 'account/login.html', {"form": form})
