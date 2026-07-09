from flask import Flask
from flask_talisman import Talisman

app = Flask(__name__)

app.config["SECRET_KEY"] = "dev-secret-key"

Talisman(
    app,
    force_https=False,
    content_security_policy=None,
)

@app.route("/")
def index():
    return {"message": "DevOps Capstone Service is running"}

from service import routes
