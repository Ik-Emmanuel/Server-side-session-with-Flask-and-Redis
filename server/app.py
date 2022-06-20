from flask import Flask, jsonify, request, abort, session
from flask_bcrypt import Bcrypt
from models import User, db
from config import ApplicationConfig
from flask_session import Session

app = Flask(__name__)
app.config.from_object(ApplicationConfig)
server_session = Session(app)

bcrypt = Bcrypt(app)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/register", methods =["POST"])
def register_user():
    email = request.json["email"]
    password = request.json["password"]
    user_exists = User.query.filter_by(email=email).first() is not None

    if user_exists:
        # abort(409)
        return jsonify({"error": "user with email already exists"}), 409

    hashed_password = bcrypt.generate_password_hash(password)
    new_user = User(email=email, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify ({
        "id": new_user.id,
        "email": new_user.email
    })

@app.route("/login", methods=["POST"])
def login_user():
    email = request.json["email"]
    password = request.json["password"]
    user = User.query.filter_by(email=email).first()

    if not user:
        return jsonify({"error": "Not a registered user"}), 404

    if not bcrypt.check_password_hash(user.password, password):
        return jsonify({"error": "Unauthorized"}), 401

    # we can use flask's session because we configures server_session = Session(app) else this will be expose to client with the normal session
    session["user_id"] = user.id

    return jsonify ({
        "id": user.id,
        "email": user.email
    })


@app.route("/me")
def get_current_user():
    user_id = session.get("user_id")

    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    user = User.query.filter_by(id=user_id).first()
    return jsonify ({
        "id": user.id,
        "email": user.email
    })


if __name__ == "__main__":
    app.run(debug=True)