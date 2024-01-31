from flask import Flask

app = Flask(__name__)

@app.route("/") # the route, or the empty route that lands us to the homepage
def hello_world():
    return "Hello, World!"

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)