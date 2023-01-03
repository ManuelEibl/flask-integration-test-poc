from flask import Flask

from app.database.base import db
from app.database.models import Product


def test_get_returns_correct_data(test_app: Flask):
    test_product = Product("name", "description", 10, 5)
    with test_app.app_context():
        db.session.add(test_product)
        db.session.commit()

    resp = test_app.test_client().get("/products")
    assert resp.status_code == 200
    data = resp.get_json()
    assert len(data) == 1
    product = data[0]
    assert product["name"] == "name"
    assert product["description"] == "description"
    assert product["price"] == float(10)
