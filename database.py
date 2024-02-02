from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
import os



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

def load_job_from_db(id):
  with engine.connect() as conn:
      result = conn.execute(
          text("SELECT * FROM jobs WHERE id = :val"), {"val": id}
      )
      row = result.fetchone()

      if row is None:
          return None
      else:
          job_dict = {}
          for column, value in zip(result.keys(), row):
              job_dict[column] = value
          return job_dict

from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

def add_application_to_db(job_id, application):
  query = """
  INSERT INTO applications (job_id, fullname, email, linkedin_url, education, work_experience, resume_url)
  VALUES (:job_id, :fullname, :email, :linkedin_url, :education, :work_experience, :resume_url)
  """

  params = {
      "job_id": job_id,
      "fullname": application.get('fullname', ''),
      "email": application.get('email', ''),
      "linkedin_url": application.get('linkedin_url', ''),
      "education": application.get('education', ''),
      "work_experience": application.get('work_experience', ''),
      "resume_url": application.get('resume_url', ''),
  }

  try:
      with engine.connect() as conn:
          statement = text(query).bindparams(**params)
          conn.execute(statement)
  except SQLAlchemyError as e:
      print(f"Error adding application to the database: {str(e)}")
      raise