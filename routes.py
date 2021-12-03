from flask import Flask, request
from database import insert_user

app = Flask("Youtube")


@app.route("/helloworld", methods=["GET"])
def hello_world():
    return {"Hello": "World"}


@app.route("/register/user", methods=["POST"])
def register_user():
    body = request.get_json()

    if "name" not in body:
        return generate_response(400, "The parameter 'name' is required.")

    if "email" not in body:
        return generate_response(400, "The parameter 'email' is required.")

    if "password" not in body:
        return generate_response(400, "The parameter 'password' is required.")

    user_name = insert_user(body["name"], body["email"], body["password"])

    return generate_response(200, "Created User", 'user', user_name)


def generate_response(status, message, content_name=False, content=False):
    response = {"status": status, "message": message}

    if content_name and content:
        response[content_name] = content

    return response



if __name__ == '__main__':
    app.run()
