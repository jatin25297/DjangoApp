from django.shortcuts import render, redirect
from datetime import datetime
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup_view(request):
    today=datetime.now()

    return render(request, 'index.html',{'today':today})