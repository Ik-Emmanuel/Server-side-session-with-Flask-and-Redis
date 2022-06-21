from redis_om import get_redis_connection, HashModel
from flask import Flask, jsonify, request, abort, session


app = Flask(__name__)


redis = get_redis_connection(
    host="localhost",
    port=6379,
    decode_responses = True
)

class Product(HashModel):
    name:str
    price:float
    quantity:int

    class Meta:
        database = redis


def format(pk: str):
    product = Product.get(pk)
    return {
        'id':product.pk,
        'name': product.name, 
        'price': product.price,
        'quantity': product.quantity
    }


@app.route("/products", methods =["GET", "POST"])
def register_product():
    if request.method == "POST":
        name = request.json["name"]
        price = request.json["price"]
        quantity = request.json["quantity"]

        new_product = Product(name=name, price=price, quantity=quantity)
        new_product.save()
        return jsonify ({"success": "Product added"})
        
    data = [format(pk) for pk in Product.all_pks()]
    return jsonify({"data": data})




if __name__ == "__main__":
    app.run(debug=True)