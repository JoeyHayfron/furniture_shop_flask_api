import os
from . import create_app
app = create_app(os.getenv("CONFIG_MODE"), __name__)
from .urls import product
