import os
from app import create_app
from app.config import config

app = create_app(os.environ.get("CONFIG_MODE"), __name__)

print(f"{os.environ.get('CONFIG_MODE')}  {config[os.environ.get('CONFIG_MODE')]}")


@app.route("/")
def get_home():
    return "Working now"


from app.urls import product
