from django.shortcuts import render

# Create your views here.

def About(request):
    return render(request,'About.html')

def E_brochures(request):
    return render(request,'E_brochures.html')

def E_Newsletter(request):
    return render(request,'E_Newsletter.html')

def Experience_kerala(request):
    return render(request,'Experience_kerala.html')

def Festivals(request):
    return render(request,'Festivals.html')

def Kerala_tourism(request):
    return render(request,'Kerala_tourism.html')

def Plan_your_trip(request):
    return render(request,'Plan_your_trip.html')

def Things_to_do(request):
    return render(request,'Things_to_do.html')

def Where_to_go(request):
    return render(request,'Where_to_go.html')

def Where_to_stay(request):
    return render(request,'Where_to_stay.html')