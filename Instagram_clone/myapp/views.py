from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

# Create your views here.

def signup_view(request):

    return render(request, 'index.html')