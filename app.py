#correo = "andre@g.com"
#nombre = "german"

#lista
#correos = [ "victor@susi.com","edgar@susi.com","mau@susi.com","alfredito@susi.com"]


#indices         0                1                 2              3
#print(nombre)

#listas 

#print(correos[0]) se imprime solo el slot seleccionado

#slice [inicio, final]

#print(correos[0:2]) se mostrara el pedazo mostrado desde el princio hasta uno antes

#correos.append("foo@foo.com") agrega algo a una lista
#del correos [0] elimnita un elemnto con el indice asignado
#correo.insert(0,"foo@foo.com") inserta un nuevo elemento en el indice asignado
#correos.pop() elimina el ultimo elemento o el elemento del indice asignado
#correos.remove("mau@susi.com") elimina el elemento asignado pd: no es por indice sino el valor o elemento nombrado
#correos.insert(0,"foo@foo.com")

#total = len(correos) #len funcion para calcular total de items
#for indice in range(total):
#    print(correos[indice])

#edad = 21
#if edad <19 : 
#    print("eres mayor")

#contador =0
#limite = len(correos)
#while contador < limite:
#    print(correos[contador])
#    contador+=1

#def mostrar_mensaje(alias): ---- def nombre de la funcion (parametros x,y,z)
#    mensaje = "hola desde python " + alias
#    return mensaje

#contenido = mostrar_mensaje("bar")
#print(contenido)

#import arch1 ----- importar modulo
#arch1.mostrar_arch1             
#import arch1 as a  ------------- se puede abreviar el modulo para llamarlo de cierta manera como 1 letra
#print(a.mostrar_arch1)
#from arch1 import * (todo lo q esta en arch1) or (algo en especeficio)

#diccionario

#perfil_usuario = {
#    "correo":"foo@foo.com",
#    "nombre":"foo",
#    "planeta":"tierra"
#}

#perfil_usuario.get("")
#perfil_usuario.clear()
#del perfil_usuario[]
#perfil_usuario.pop()
#perfil_usuario[valor nuevo] = respectivo valor
#perfil_usuario.update({"x"="y"})
#perfil_usuario.copy()

#print(perfil_usuario) 

#lista_a = ["a","b","c"]
#lista_b = [*lista_a,"d","e"]

#tubla = {"foo","bar","baz"} listas q no se pueden alterar su contenido

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    "<p>Hello, World!</p>"

    return render_template("index.html")
