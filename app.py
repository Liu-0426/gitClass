from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "Hello Git Students!"}

if __name__ == "__main__":
    app.run(debug=True)


# Fix function
# @app.route("/")
# def home():
#     return {"message": "Welcome to Git Class! This code has been updated."}


# add API
# @app.route("/hello/<name>")
# def hello(name):
#     return {"message": f"Hello, {name}!"}
