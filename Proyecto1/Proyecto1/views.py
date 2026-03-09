from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template import loader
from django.shortcuts import render

class Persona(object):
    def __init__(self, nombre, apellido):
        self.nombre=nombre
        self.apellido=apellido

def saludo(request):   #primera vista

    p1=Persona("Juan","Diaz") 

   # nombre = "Caye"
    #apellido="Benitez"
    ahora=datetime.datetime.now()
    temas_curso=["Plantillas","si","mno"]

   # doc_externo=open("C:/Users/usuario/OneDrive/Escritorio/Proyecto_Django_Windows/Proyecto1/Proyecto1/layouts/plantilla.html")

    #plt=Template(doc_externo.read())

    #doc_externo.close()
    #doc_externo=loader.get_template('plantilla.html')
    #ctx=Context({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha":ahora, "temas":temas_curso})

    #documento=doc_externo.render({"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha":ahora, "temas":temas_curso})
    return render(request, "plantilla.html",{"nombre_persona":p1.nombre, "apellido_persona":p1.apellido, "fecha":ahora, "temas":temas_curso})

def despedida(request): #segunda vista
    return HttpResponse("Hasta aqui llegamos")


def hora_fecha(request): #parametro
    fecha_actual=datetime.datetime.now()
    documento="""<html>
    <body>
    <h1>Hola mundo</h1> %s
    </body>
    </html>""" %fecha_actual

    return HttpResponse(documento)


def CalculaEdad(request,edad, agno):
    periodo =agno-2026
    edadFutura =edad+periodo
    documento='''<html>
    <body>
    <h2>
    En el año %s tendras %s
    </h2>
    </body>
    </html>'''%(agno, edadFutura)
    return HttpResponse(documento)

def cursoC(request):
    fecha_actual=datetime.datetime.now()
    return render(request,"CursoC.html",{"hora_fecha":fecha_actual})
