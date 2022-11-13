from django.shortcuts import render
from haversine import haversine, Unit
# Create your views here.
def home(request):
    return render(request,'home.html')