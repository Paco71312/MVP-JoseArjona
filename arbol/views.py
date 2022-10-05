from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.shortcuts import render

from arbol.models import Familiar

def crear_familiar(request,nombre,apellido,edad):
    familiar=Familiar(nombre=nombre,apellido=apellido,edad=edad,fecha_creacion=datetime.now())
    familiar.save()
    template=loader.get_template('arbol/crear_familiares.html')
    renderizar_template=template.render({'familiar':familiar})        
    return HttpResponse(renderizar_template)

def ver_familiar(request):
    familiar=Familiar.objects.all
    return render(request,'arbol/ver_familiar.html',{'familiar':familiar})
    
