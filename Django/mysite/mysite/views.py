from django.http import HttpResponse
from django.shortcuts import render


def aboutus(request):
    return HttpResponse("Youexcel Institute")

def program(request,id):
    return HttpResponse(id)

def home(request):
    return render(request,'index.html')
def Pythoncourse(request):
    return HttpResponse("<b>program A,program A<b>")

