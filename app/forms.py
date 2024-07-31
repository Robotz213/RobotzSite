from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, EmailField, TextAreaField
from wtforms.validators import DataRequired, ValidationError
import phonenumbers

class ContactForm(FlaskForm):
    
    full_name = StringField("Seu Nome", validators = [DataRequired()])
    email_address = EmailField("Seu E-Mail", validators = [DataRequired()])
    phone = StringField("Seu telefone", validators = [DataRequired()])
    Message = TextAreaField("Sua Mensagem", validators = [DataRequired()])
    submit = SubmitField("Enviar!")
