from flask import Flask, render_template, request, redirect
import controlador_carros

app = Flask(__name__)

@app.route("/agregar_carro")
def formulario_agregar_carro():
    return render_template("agregar_carro.html")

@app.route("/guardar_carro", methods=["POST"])
def guardar_carro():
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    color = request.form["color"] 
    precio = float(request.form["precio"])
    cuotas = int(request.form["cuotas"])
    controlador_carros.insertar_carros(marca, modelo, color, precio, cuotas)
    return redirect("/carros")

@app.route("/")
@app.route("/carros")
def carros():
    carros = controlador_carros.obtener_carros()
    return render_template("carros.html", carros=carros)


@app.route("/eliminar_carro", methods = ["POST"])
def eliminar_carro():
    controlador_carros.eliminar_carros(request.form["id"])
    return redirect("/carros")


@app.route("/formulario_editar_carro/<int:id>")
def editar_carro(id):
    carro = controlador_carros.obtener_carros_por_id(id)
    return render_template("editar_carro.html", carro = carro)


@app.route("/actualizar_carro", methods=["POST"])
def actualizar_carro():
    id = request.form["id"]
    marca = request.form["marca"]
    modelo = request.form["modelo"]
    color = request.form["color"] 
    precio = float(request.form["precio"]) 
    cuotas = int(request.form["cuotas"])
    controlador_carros.actualizar_carros(marca, modelo, color, precio, cuotas, id)
    return redirect("/carros")


#Iniciar el servidor
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 8000, debug = True)