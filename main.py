from flask import Flask,request,render_template,make_response

app=Flask(__name__)

listado=[]

@app.route('/buscar')
def buscar():
    producto = request.args.get('producto')
    talla = request.args.get('tamano')
    color = request.args.get('color')
    if producto is None and talla is None and color is None:
        return "faltan datos para busqueda"
    return f"Buscando {producto} de talla {talla} y color {color}"

@app.route("/registro", methods=["GET"]) 
def ruta_formulario():
    return render_template("formulario.html")

@app.route("/registro", methods=["POST"]) 
def ruta_registro():
    nombre=request.form.get("estudiante")
    email=request.form.get("correo")
    password=request.form.get("contrasena")
    if nombre and email and password:
        listado.append({"nombre":nombre,"correo":email,"password":password,})
        return render_template("formulario.html", listado=listado)
    
    return f"faltan datos"

    #return f"usuario resgistrado: {nombre}, {email}, {password}"

#tipo de solicitud 3: Parametros en la ruta

@app.route("/ropa/<string:producto>")
def ruta_consulta(producto, talla):
    return f"el producto consultado es {producto}, {talla}"

#tipo de solicitud 4: headers http

@app.route("/ver-headers")
def ruta_headers():
    navegador=request.headers.get("User-agent")
    return f"el navegador que hace la peticion es {navegador}"

#tipo de solicitud 5: manejo de cookies 

@app.route("/crear-cookie")
def crear_cookie():
    respuesta=make_response("cookie-creada")
    respuesta.set_cookie("usuario_logeado","true")
    return respuesta


@app.route("/leer-cookie")
def leer_cookie():
    valor=request.cookies.get("usuario_logeado")
    return f"el valor de la cookie es: {valor}"


if __name__=="__main__":
    app.run(debug=True)