from flask import Flask, render_template

app = Flask(__name__)

@app.route("/") # the route, or the empty route that lands us to the homepage
def hello_template():
    return render_template('home.html')

print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)