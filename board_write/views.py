from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Board_write
# Create your views here.

def new(request) :
    return render(request,'new.html')