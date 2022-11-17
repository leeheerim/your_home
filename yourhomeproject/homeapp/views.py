from django.shortcuts import render
from .models import table
from django.db.models import Q

# Create your views here.
def home(request):

    return render(request,'home.html')

