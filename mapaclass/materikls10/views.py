from django.shortcuts import render
from django.template import loader 
from django.http import HttpResponse


# Create your views here.
def index(request): 
    template = loader.get_template('index.html') 
    return HttpResponse(template.render())

def peluang(request):
    template = loader.get_template('peluang.html')
    return HttpResponse(template.render())

def BarisandanDeret(request):
    template = loader.get_template('BarisandanDeret.html')
    return HttpResponse(template.render())

def Eksponen(request):
    template = loader.get_template('Eksponen.html')
    return HttpResponse(template.render())

def LogIn(request):
    template = loader.get_template('LogIn.html')
    return HttpResponse(template.render())

def LogOut(request):
    template = loader.get_template('LogOut.html')
    return HttpResponse(template.render())

def Referensi(request):
    template = loader.get_template('Referensi.html')
    return HttpResponse(template.render())

def Statistika(request):
    template = loader.get_template('Statistika.html')
    return HttpResponse(template.render())

def Profil(request):
    template = loader.get_template('Profil.html')
    return HttpResponse(template.render())