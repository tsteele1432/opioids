from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def indexPageView(request):
    return render(request, "myDrugs/index.html")

def searchPageView(request):
    return HttpResponse("This is search")

def detailsPageView(request):
    return HttpResponse("This is details")