# Add the following import
from django.http import HttpResponse
from django.shortcuts import render

# fake data just for now 
# Add the SurvivalGarden class & list and view function below the imports
class SurvivalGarden:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, description, age):
    self.name = name
    self.description = description
    self.age = age

survivalgardens = [
  SurvivalGarden('Tropical', 'Garden for tropical climates.', 3),
  SurvivalGarden('Desert', 'Garden for dry climates.', 6),
  SurvivalGarden('Deciduous', 'Garden for Southern Ontario.', 9),
  SurvivalGarden('Boreal', 'Garden for Northern Ontario.', .9)
]

def index(request):
    #return HttpResponse("list of survivalgardens")
    return render(request, 'survivalgardens/index.html', { "survivalgardens": survivalgardens } )


def about(request):
  return render(request, 'about.html')

def home(request):
    return HttpResponse("<h1> HELLO G'WORLD </h1>")


