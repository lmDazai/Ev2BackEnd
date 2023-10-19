from django.shortcuts import render

def index(request):
    return render(request,'templatesApp/index.html')


def chile(request):
    data={
        "titulo": "Chile",
        'producto1':"MAC",
        'producto2':"Celular",
        'producto3':"PlayStation",
        'imagen':'imagenes/productos.jpg'
    }
    return render(request,'templatesApp/info.html')

def argentina(request):
    data={
        "titulo": "Argentina",
        'producto1':"Pelota",
        'producto2':"Figuera de Accion",
        'producto3':"Juego de Mesa",
        
    }
    return render(request,'templatesApp/info.html')

def peru(request):
    data={
        "titulo": "Peru",
        'producto1':"POlera",
        'producto2':"Chaqueta",
        'producto3':"ZApatilla",
        
    }
    return render(request,'templatesApp/info.html')

# Create your views here.
