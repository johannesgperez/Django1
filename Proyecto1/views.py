import datetime
from datetime import datetime
from django.http import HttpResponse
from django.template import Template, Context

def saludo(request):
    return HttpResponse("Hola Mundo!!!")

def segunda_vista(request):
    return HttpResponse("Django es muy sencillo")

def diaHoy(request):
    dia = datetime.datetime.now()
    documento_texto = f"Hoy es dia: <br> {dia}"
    return HttpResponse(documento_texto)

def miNombre(request, nombre):
    texto = f"Mi nombre es {nombre}"
    return HttpResponse(texto)

def year(request, age):
    age = int(age)
    current_year = datetime.today().year
    year_born = current_year - age
    text_year = f"<h1>Usted nació el año {year_born}<h1>"
    return HttpResponse(text_year)

def probandoTemplate(request):
    miHtml = open("C:/Users/Johannes/Desktop/Proyecto1/plantillas/template.html") # ojo con el \t por eso uso /, otra opcion es renombrar el archivo template
    plantilla = Template(miHtml.read())
    miHtml.close()
    miContexto = Context()
    documento = plantilla.render(miContexto)
    return HttpResponse(documento)


    
    



