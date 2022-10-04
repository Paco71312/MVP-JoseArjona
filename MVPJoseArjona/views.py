from django.http import HttpResponse
from django.template import Context,Template,loader
from datetime import datetime

from arbol.models import Familiar

def crear_familiar(request,nombre,apellido,edad):
    familiar=Familiar(nombre=nombre,apellido=apellido,edad=edad,fecha_creacion=datetime.now())
    familiar.save()
    template=loader.get_template('crear_familiares.html')
    renderizar_template=template.render({'familiar':familiar})        
    return HttpResponse(renderizar_template)

def ver_familiar(request):
    familiar=Familiar.objects.all
    template=loader.get_template('ver_familiar.html')
    renderizar_template=template.render({'familiar':familiar})
    return HttpResponse(renderizar_template)