from flask import Flask, render_template, jsonify
from database import engine
from sqlalchemy import text

app = Flask(__name__)


@app.route("/")
def hello_template():
    jobs = load_jobs_from_db()
    return render_template('home.html', jobs=jobs, company_name='Fluskë')

@app.route("/api/jobs")
def list_jobs():
    jobs = load_jobs_from_db()  # Call the function to load jobs from the database
    return jsonify(jobs)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
