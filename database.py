from sqlalchemy import create_engine, text
import os

def load_jobs_from_db():
  with engine.connect() as conn:
      result = conn.execute(text("SELECT * FROM jobs"))
      jobs = []
      for row in result.fetchall():
          job_dict = {}
          for column, value in zip(result.keys(), row):
              job_dict[column] = value
          jobs.append(job_dict)
      return jobs

# Use os.environ to access environment variables
db_config = {
    'host': os.environ.get('DB_HOST'),
    'username': os.environ.get('DB_USERNAME'),
    'password': os.environ.get('DB_PASSWORD'),
    'name': os.environ.get('DB_NAME')
}

# Check if any of the required environment variables are missing
if None in db_config.values():
    raise ValueError("One or more required environment variables are missing.")

# Create the database engine
db_connection_string = f"mysql+pymysql://{db_config['username']}:{db_config['password']}@{db_config['host']}/{db_config['name']}"

engine = create_engine(db_connection_string, connect_args={"ssl": {"ssl_ca": "/etc/ssl/cert.pem"}})

# Connect to the database and execute a query
with engine.connect() as conn:
  result = conn.execute(text("SELECT * FROM jobs"))

  result_dicts = []
  for row in result.all():
    result_dicts.append(row._asdict())


