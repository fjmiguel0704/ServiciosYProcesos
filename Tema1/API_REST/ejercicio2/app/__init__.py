from flask import *
from .autor.routes import autorBP
from .libro.routes import libroBP

app = Flask(__name__)

app.register_blueprint(autorBP, url_prefix='autores')
app.register_blueprint(libroBP, url_prefix='libros')