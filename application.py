from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/st")
def st():
    return "Hello from st route!"

# if __name__ == "__main__":
#     app.run()
