from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Esta aplicación será un "To Do List".
#Por cada To Do List, tendremos varios Items relacionados.
#Por tanto tendremos una clase para nuestro onjeto TodoList
#y otra clase para nuestros itemes que estan unidos a una sola TodoList
#Nuestra relación será muchos es a uno.

class TodoList(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="todolist", null=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):
    '''
    El item creado quedará conectado a la foreingkey de la TodoList que le corresponda.

    on_delete: Si la TodoList es eliminada, el item relacionado a ella también lo será.
    CASCADE: Indica la manera en que es eliminada.
    '''

    todolist = models.ForeignKey(TodoList, on_delete=models.CASCADE) #a cuál TodoList pertenece
    text = models.CharField(max_length=300) #texto explicativo del item
    complete = models.BooleanField() #opción Hecho!

    def __str__(self):
        return self.text


