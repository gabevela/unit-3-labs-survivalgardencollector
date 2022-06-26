# Add the following import
from django.http import HttpResponse
from django.shortcuts import render

# fake data just for now 



def about(request):
  return render(request, 'about.html')

def home(request):
    return HttpResponse("<h1> HELLO G'WORLD </h1>")


