from django.shortcuts import render, redirect

# Create your views here.

def info(request):
    return redirect('info')

def people(request):
    return redirect('people.html')
