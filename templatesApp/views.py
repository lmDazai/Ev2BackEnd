from django.shortcuts import render

def index(request):
    return render(request,'templatesApp/index.html')


def chile(request):
    data={
        "titulo": "Electronica",
        'producto1':"Intro",
        'producto2':"Inicio",
        'producto3':"Desarrollo",
        'producto4':"Final",
        'iemagn':'imagenes/chile.png'
    }
    return render(request,'templatesApp/info.html')

def argentina(request):
    data={
        "titulo": "Argentina",
        'producto1':"Intro",
        'producto2':"Inicio",
        'producto3':"Desarrolo",
        'producto4':"Final",
        'iemagn':'imagenes/argentina.jpg'
        
    }
    return render(request,'templatesApp/info.html')

def peru(request):
    data={
        "titulo": "Peru",
        'producto1':"Intro",
        'producto2':"Inicio",
        'producto3':"Desarrollo",
        'producto4':"Final",
        'iemagn':'imagenes/peru.jpg'
        
    }
    return render(request,'templatesApp/info.html')

# Create your views here.
