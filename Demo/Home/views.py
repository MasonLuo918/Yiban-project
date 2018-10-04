from django.shortcuts import render
from .models import ImageDisplay
# Create your views here.

def home(request):
    Images = ImageDisplay.objects.filter(Display=True)
    return render(request,"home/Home.html",{"Images":Images})