import os

from . import create_app

app = create_app(os.getenv("CONFIG_MODE"), __name__)


@app.route("/")
def get_home():
    return 'Working now'
