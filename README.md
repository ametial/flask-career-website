
# Flask Career Website

## Overview
This is a Flask-based web application for a career and job listing website.

## Tech Stack
- Flask
- Python
- HTML/CSS
- SQLAlchemy
- SQLite/PostgreSQL

## Setup & Installation
1. Clone the repository:
   ```
   git clone https://github.com/ametial/flask-career-website.git
   ```
2. Create a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Initialize the database:
   ```
   flask db init
   flask db migrate
   flask db upgrade
   ```
5. Run the app:
   ```
   flask run
   ```

## Usage
After launching, visit `http://localhost:5000` in your browser.

## Contributing
Contributions are welcome. Please adhere to standard Git workflow.

## License
This project is licensed under the MIT License.

## Future Improvements
- User Authentication
- Responsive Design
- API Integration
- Unit and Integration Tests
- Docker Integration
- CI/CD Pipeline


