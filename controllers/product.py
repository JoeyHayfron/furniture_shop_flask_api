from uuid import uuid4

from flask import request, jsonify

from .. import db
from ..models.product import Product


def list_all_products():
    products = db.paginate(db.select(Product))
    response = []
    print(f"PRODUCTS: {products}")
    for product in products: response.append(product.toDict())
    return jsonify(response)


def create_product():
    try:
        request_form = request.get_json(force=True)
        id = str(uuid4())
        new_product = Product(id=id, product_name=request_form['product_name'], description=request_form['description'],
                              price=request_form['price'], type=request_form['type'], img=request_form['img'])
        db.session.add(new_product)
        db.session.commit()
        response = Product.query.get(id).toDict()
        return jsonify(response)
    except Exception as e:
        print(f"Exception: {e}")
        return None
