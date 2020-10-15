from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.shortcuts import render
from django.http import JsonResponse
#templates
def citas(request): 
    return render(request,'citas.html')

def medicos(request):
    return render(request,'medicos.html')

def pacientes(request): 
    return render(request,'pacientes.html')

def index(request): 
    return render(request,'home.html')

def historial(request): 
    return render(request,'historial.html')
  

#consultas

@csrf_exempt
def send_json(request):
    codigo=request.POST['user']
    data = [{'user':codigo}]
    return JsonResponse(data, safe=False)
