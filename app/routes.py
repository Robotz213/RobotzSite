from flask import jsonify
from flask import request
from flask import redirect
from flask import render_template
from flask import flash
from flask import url_for
from flask import session

from flask_mail import Message
from flask_wtf import FlaskForm
from typing import Type

from app import app
from app import mail
from app.forms import ContactForm
from app.handler import *

@app.route("/", methods=["GET", "POST"])
def index():

    form: Type[ContactForm] = ContactForm()
    if form.validate_on_submit():

        robot = f"Robotz Form"
        assunto = "Notificação de Formulário"
        destinatario = "nicholas@robotz.dev"
        formatted_message = form.Message.data.replace('\n', '<br>')
        mensagem = f""" <h1>Alguém preencheu seu formulário!</h1>
                        <br>
                        <h3>De: {form.full_name.data} </h3>
                        <h3>Email: {form.email_address.data} </h3>
                        <h3>Mensage:</h3>
                        <p>{formatted_message}</p>
        """

        msg = Message(assunto, sender=robot, recipients=[
                      destinatario], html=mensagem)
        mail.send(msg)
        session["message"] = 'Sua mensagem foi enviada!'
        flash('Sua mensagem foi enviada!', "success")
        return redirect(url_for("index"))

    return render_template("index.html", form=form, message=session.get("message", ""))
