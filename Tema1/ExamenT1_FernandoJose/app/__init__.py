import secrets
import string
from flask import Flask
from flask_jwt_extended import JWTManager

from app.departamento.routes import departamentoBP
from app.proyecto.routes import proyectoBP
from app.users.routes import usersBP

longitud = 15
claveSegura = "".join(secrets.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(longitud))

app = Flask(__name__)
app.config['SECRET_KEY'] = claveSegura
jwt = JWTManager(app)

app.register_blueprint(departamentoBP, url_prefix="/departamento")
app.register_blueprint(proyectoBP, url_prefix="/proyecto")
app.register_blueprint(usersBP, url_prefix="/users")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5050)