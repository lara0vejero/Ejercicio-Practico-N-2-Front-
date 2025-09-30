from flask import Flask, render_template, request, redirect, flash, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'amigosporeldeporte123@gmail.com'
app.config['MAIL_PASSWORD'] = '...'
app.config['MAIL_DEFAULT_SENDER'] = 'amigosporeldeporte123@gmail.com'

mail = Mail(app)

info_evento = {
    "nombre" : "Rally MTB 2025",
    "organizador" : "Club Social y Deportivo Unidos por el Deporte",
    "descripcion" : "Carrera MTB rural en dos modalidades 30km y 80 km",
    "fecha" : "24 de octubre de 2025",
    "horario" : "8am",
    "lugar" : "Tandil, Buenos Aires",
    "tipo_carrera" : "MTB rural",
    "modalidad_costo" : { 1 : {"nombre" : "corta", "valor" : "100"},
                          2 : {"nombre" : "larga", "valor" : "200"}},                                    
}          

@app.route("/")
def index():
    return render_template("index.html", info = info_evento)

@app.route("/about")
def informacion():
    return render_template("about.html", info = info_evento)

@app.route("/registrarse", methods=["GET", "POST"])
def registrarse():
    if request.method == "POST":
        nombre_completo = request.form.get("nombre")
        edad = request.form.get("edad")
        telefono = request.form.get("telefono")
        mail_participante = request.form.get("mail")
        categoria = request.form.get("categoria")

        msg = Message(
            subject = "Nueva inscripción",
            recipients = [mail_participante] 
        )

        msg.html = render_template("mail.html", 
                                   nombre_completo = nombre_completo, 
                                   edad = edad, 
                                   telefono = telefono, 
                                   mail_participante = mail_participante, 
                                   categoria = categoria
                                   )
        
        mail.send(msg) 
        return redirect(url_for("registrarse"))
    else:
        return render_template("registration.html", info = info_evento)


@app.route("/importante")
def importante():
    return render_template("importante.html", info = info_evento)


if __name__ == "__main__":
    app.run("localhost", port=8080, debug=True)