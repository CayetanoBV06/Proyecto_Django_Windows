from django.http import HttpResponse
import datetime
from django.template import Template, Context

def saludo(request):   #primera vista 
    doc_externo=open("C:/Users/usuario/OneDrive/Escritorio/Proyecto_Django_Windows/Proyecto1/Proyecto1/layouts/plantilla.html")

    plt=Template(doc_externo.read())

    doc_externo.close()

    ctx=Context()

    documento=plt.render(ctx)
    return HttpResponse(documento)

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