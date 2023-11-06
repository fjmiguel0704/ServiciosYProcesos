import secrets
import string
from flask import Flask
from flask_jwt_extended import JWTManager

from .autor.routes import autorBP
from .libro.routes import libroBP
from .users.routes import usersBP

longitud = 15
claveSegura = "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longitud))

app = Flask(__name__)
app.config['SECRET_KEY'] = claveSegura
jwt = JWTManager(app)

app.register_blueprint(autorBP, url_prefix="/autor")
app.register_blueprint(libroBP, url_prefix="/libro")
app.register_blueprint(usersBP, url_prefix="/users")