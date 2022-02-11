from flask import Flask, escape, request, render_template
from jinja2 import environmentfilter ##importar de la libreria

app = Flask (__name__) ##inicializamos la app con el nombre

@app.route('/')  ## definimos que en la ruta de inicio sera aplicada la funcion hola.
def hola():
    return 'Hi Penguins!'

##app.run (debug=True)

@app.route('/coach') ##creamos la ruta coach
def hola_coaches(): ##definimos la funcion que sera devuelta
    nombre= 'Arami' ##inicializamos un dato
    devolver =  request.args.get('nombre', nombre) ##definimos que sera devuelto y renderizado
    return f'hola,{escape(devolver)}' ##retornamos al html
    


@app.route('/inicio') ##creamos la ruta inicio
def inicio():
    return render_template('inicio.html')



@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

app.run (debug=True)

