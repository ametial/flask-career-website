from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    'id': 1,
    'title': 'Data Analyst',
    'location': 'Berlin, Germany',
    'salary': '€60.000'
  },
  
  {
    'id': 2,
    'title': 'Software Engineer',
    'location': 'Berlin, Germany or Remote',
    'salary': '€60.000'
  },
  
  {  
  'id': 3,
  'title': 'Cyber Security Engineer',
  'location': 'Berlin, Germany or Remote',
  'salary': '€60.000'
  },

  {  
  'id': 4,
  'title': 'Cyber Security Engineer',
  'location': 'Berlin, Germany or Remote'
  }

]

@app.route("/") # the route, or the empty route that lands us to the homepage
def hello_template():
    return render_template('home.html', jobs=JOBS, company_name='Fluskë')

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)
  
print(__name__)
if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True)


