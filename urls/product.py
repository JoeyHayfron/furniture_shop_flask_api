from flask import request

from ..controllers.product import list_all_products, create_product
from ..server import app


@app.route('/products', methods=['GET', 'POST'])
def list_create_products():
    if request.method == 'GET':
        return list_all_products()
    elif request.method == 'POST':
        return create_product()
