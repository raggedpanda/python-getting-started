from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

@login_required
def index(request):
    return render(request, 'index.html',{})

@login_required
def data(request):
    return render(request, 'data.html',{})

@login_required
def outliers(request):
    return render(request, 'outliers.html',{})

@login_required
def wineTable(request):
    return render(request, 'wineTable.html',{})

@login_required
def settings(request):
    return render(request, 'settings.html',{})

def login(request):
    return render(request, 'login.html',{})

def logout_view(request):
    logout(request)

# def logout(request):
#     logout(request)
#     return render(request, 'logout.html',{})