from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Configurar banco de dados SQLite
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///contacts.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Modelo do contato
class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    whatsapp = db.Column(db.String(20))  # Adicionado WhatsApp
    message = db.Column(db.Text)

# Rota principal
@app.route("/", methods=["GET", "POST"])
def landing():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        whatsapp = request.form["whatsapp"]  # Captura WhatsApp também

        contact = Contact(name=name, email=email, whatsapp=whatsapp, message="")
        db.session.add(contact)
        db.session.commit()

        return redirect(url_for("thank_you"))  # Direciona para a página de agradecimento

    return render_template("index.html")

# Rota de agradecimento
@app.route("/thankyou")
def thank_you():
    return render_template("thankyou.html")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
