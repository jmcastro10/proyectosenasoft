from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.shortcuts import render
from django.http import JsonResponse

def saludo(request): 
    return render(request,'base.html')

def index(request): 
    return render(request,'home.html')
  
@csrf_exempt
def send_json(request):
    codigo=request.POST['user']

    data = [{'user':codigo}]
    return JsonResponse(data, safe=False)
