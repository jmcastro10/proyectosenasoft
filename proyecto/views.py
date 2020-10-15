from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.template.loader import get_template
from django.shortcuts import render
from django.http import JsonResponse
from django.db import connection
import psycopg2
def citas(request): 
    return render(request,'citas.html')

def pacientes(request): 
    return render(request,'pacientes.html')

def index(request): 
    return render(request,'home.html')
  

@csrf_exempt
def send_json(request):
    codigo=request.POST['user']

    data = [{'user':codigo}]
    return JsonResponse(data, safe=False)

@csrf_exempt
def test(request):
    data = []
    #sql='SELECT * FROM proyecto_medicos WHERE "_idMedico" = 5'
    sql= "INSERT INTO proyecto_medicos values ('5','juac', 'correa','herazo@meet.com', 313456529)"
    data = setQuery(sql)      
    return JsonResponse(data, safe=False)

#def getQuery(sql):
    #data = []
    #db = psycopg2.connect("dbname=hospital user=postgres password=admin")
    #cursor = db.cursor()
    #cursor.execute(sql)
    #rows = cursor.fetchall()
    #for row in rows:
        #data.append(row)
    #db.close()
    #if len(data) == 0:
       # data.append({0:'no hay dato'})
    #return data

def setQuery(sql):
    data=[]     
    try:
        db = psycopg2.connect("dbname=hospital user=postgres password=admin")    
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()
        db.close()
        data.append({0:'Datos insertados con exito'})
    except (Exception, psycopg2.Error) as error :
        data.append({0:str(error)}) 
    return data
