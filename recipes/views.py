from django.shortcuts import render

from django.http import HttpResponse

def home(request):

    return HttpResponse("<H1>Bem-Vindo á página de receitas!</h1>")
# Create your views here.
