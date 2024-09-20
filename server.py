import os
from app import create_app

app = create_app(os.environ.get("CONFIG_MODE"), __name__)


@app.route("/")
def get_home():
    return "Working now"


from app.urls import product
