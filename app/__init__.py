from flask import Flask
from flask_mail import Mail
from flask_bootstrap import Bootstrap5
import os
import dotenv
import os

from app.misc.gen_seed import generate_id

dotenv.load_dotenv()
app = Flask(__name__)
mail = Mail()
bootstrap = Bootstrap5()

env_vars = {key: os.getenv(key) for key in os.environ}

# Configurações do E-mail
app.config['MAIL_SERVER'] = env_vars["MAIL_SERVER"]
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = env_vars["EMAIL"]
app.config['MAIL_PASSWORD'] = env_vars["PASSWORD_EMAIL"]

# Configurações do Flask
app.config['PREFERRED_URL_SCHEME'] = "https"
app.config['SESSION_COOKIE_HTTPONLY'] = False
app.config['SESSION_COOKIE_SECURE'] = True
app.secret_key = generate_id()

mail.init_app(app)
bootstrap.init_app(app)

from app import routes
    
    
