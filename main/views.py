from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import TodoList, Item
from .forms import CreateNewList

# Create your views here.


def index(response, id):
    ls = TodoList.objects.get(id=id)

    # Lo sgte 
    if response.method == "POST":
        print(response.POST)
        if response.POST.get("save"):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()
        
        elif response.POST.get("newItem"):
            txt = response.POST.get("new")

            if len(txt) > 2:
                ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid input")

    return render(response, "main/lista.html", {"ls": ls})
    # ls.name hace referencia al nomnre de la TodoList que se definió más arriba.


def home(response):
    return render(response, "main/home.html", {})
    # El método render recibe 3 argumentos: response, ruta del html, diccionario con contexto.


def create(response):
    # Los sgts if son para encriptación y modificación de la base de datos:
    # POST se refiere a si es un input que será encriptado por seguridad (contraseña, modificaciones en la db, etc.)
    if response.method == "POST": 
        form = CreateNewList(response.POST)

        if form.is_valid(): # Si los datos del formularios son válidos:
            n = form.cleaned_data["name"] # Desencripta los datos
            t = TodoList(name=n) # Crea un objeto TodoList
            t.save() # Lo guarda en la db
        return HttpResponseRedirect("/%s" %t.name) # redirigimos a la pagina de la lista creada
    else:    
        form = CreateNewList()
    return render(response, "main/create.html", {"form": form})
