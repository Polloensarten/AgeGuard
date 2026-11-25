from django.shortcuts import render

def inicio(request):
       return render(request, 'web/index.html')

def login(request):
       return render(request, 'web/login.html')

def panel(request):
       return render(request, 'web/panel.html')

def acerca(request):
       return render(request, 'web/acerca.html')